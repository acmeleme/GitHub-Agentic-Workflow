/**
 * Polyfill for node:sqlite on Node.js < v22.5.0
 *
 * Root cause
 * ----------
 * @github/copilot (bundled inside @github/copilot-sdk) includes a copy of
 * undici that uses the SqliteCacheStore for HTTP-response caching.  The store
 * lazily calls `require('node:sqlite')` to get `DatabaseSync`.
 *
 * `node:sqlite` was introduced as an experimental built-in in Node.js v22.5.0.
 * Running the copilot CLI on Node.js v20 therefore throws:
 *
 *   Error [ERR_UNKNOWN_BUILTIN_MODULE]: No such built-in module: node:sqlite
 *
 * Solution
 * --------
 * better-sqlite3 exposes a synchronous `Database` class that is API-compatible
 * with `node:sqlite`'s `DatabaseSync`:
 *   - same constructor signature: new Database(path | ':memory:')
 *   - same .exec(), .prepare(), .close() methods
 *   - prepared statements share .run(), .all(), .get() signatures
 *
 * We patch two internal Node.js hooks before anything else loads:
 *
 * 1. Module._load  – intercepts require('node:sqlite') before
 *    Module._resolveFilename can throw ERR_UNKNOWN_BUILTIN_MODULE.
 *
 * 2. Module.isBuiltin – makes module.isBuiltin('node:sqlite') return true so
 *    @github/copilot/app.js's custom require() takes the "builtin" code path
 *    and calls __rootRequire('node:sqlite') instead of trying to resolve it as
 *    a filesystem path (which would then hit our Module._load patch).
 *
 * This file is loaded via NODE_OPTIONS=--require so the patches are in effect
 * for every Node.js process in the chain, including the CLI sub-processes that
 * the SDK spawns.
 */

'use strict';

const Module = require('module');

// Only apply the polyfill when node:sqlite is not natively available.
if (!Module.isBuiltin('node:sqlite')) {
  const Database = require('better-sqlite3');

  // better-sqlite3's Database constructor IS DatabaseSync:
  //   new Database(':memory:')   → in-memory database
  //   new Database('/path/file') → file-based database
  //   db.exec(sql)               → run DDL / PRAGMA statements
  //   db.prepare(sql)            → returns a statement
  //   stmt.run(...)              → execute with parameters
  //   stmt.all(...)              → fetch all rows
  //   stmt.get(...)              → fetch first row
  //   db.close()                 → close connection
  const sqliteShim = { DatabaseSync: Database };

  // 1. Intercept require('node:sqlite') before _resolveFilename throws.
  const originalLoad = Module._load;
  Module._load = function (request, parent, isMain) {
    if (request === 'node:sqlite') {
      return sqliteShim;
    }
    return originalLoad.apply(this, arguments);
  };

  // 2. Pretend node:sqlite is a known built-in so that @github/copilot/app.js
  //    takes the isBuiltin() branch and calls __rootRequire('node:sqlite'),
  //    which hits our patched Module._load above.
  const originalIsBuiltin = Module.isBuiltin.bind(Module);
  Module.isBuiltin = function (id) {
    if (id === 'node:sqlite') return true;
    return originalIsBuiltin(id);
  };
}
