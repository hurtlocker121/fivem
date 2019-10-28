import os
import subprocess
import sys

inputs = [
	'lib/internal/bootstrap/environment.js',
	'lib/internal/bootstrap/loaders.js',
	'lib/internal/bootstrap/node.js',
	'lib/internal/bootstrap/pre_execution.js',
	'lib/internal/per_context/primordials.js',
	'lib/internal/per_context/domexception.js',
	'lib/async_hooks.js',
	'lib/assert.js',
	'lib/buffer.js',
	'lib/child_process.js',
	'lib/console.js',
	'lib/constants.js',
	'lib/crypto.js',
	'lib/cluster.js',
	'lib/dgram.js',
	'lib/dns.js',
	'lib/domain.js',
	'lib/events.js',
	'lib/fs.js',
	'lib/http.js',
	'lib/http2.js',
	'lib/_http_agent.js',
	'lib/_http_client.js',
	'lib/_http_common.js',
	'lib/_http_incoming.js',
	'lib/_http_outgoing.js',
	'lib/_http_server.js',
	'lib/https.js',
	'lib/inspector.js',
	'lib/module.js',
	'lib/net.js',
	'lib/os.js',
	'lib/path.js',
	'lib/perf_hooks.js',
	'lib/process.js',
	'lib/punycode.js',
	'lib/querystring.js',
	'lib/readline.js',
	'lib/repl.js',
	'lib/stream.js',
	'lib/_stream_readable.js',
	'lib/_stream_writable.js',
	'lib/_stream_duplex.js',
	'lib/_stream_transform.js',
	'lib/_stream_passthrough.js',
	'lib/_stream_wrap.js',
	'lib/string_decoder.js',
	'lib/sys.js',
	'lib/timers.js',
	'lib/tls.js',
	'lib/_tls_common.js',
	'lib/_tls_wrap.js',
	'lib/trace_events.js',
	'lib/tty.js',
	'lib/url.js',
	'lib/util.js',
	'lib/v8.js',
	'lib/vm.js',
	'lib/worker_threads.js',
	'lib/zlib.js',
	'lib/internal/assert.js',
	'lib/internal/assert/assertion_error.js',
	'lib/internal/async_hooks.js',
	'lib/internal/buffer.js',
	'lib/internal/cli_table.js',
	'lib/internal/child_process.js',
	'lib/internal/cluster/child.js',
	'lib/internal/cluster/master.js',
	'lib/internal/cluster/round_robin_handle.js',
	'lib/internal/cluster/shared_handle.js',
	'lib/internal/cluster/utils.js',
	'lib/internal/cluster/worker.js',
	'lib/internal/console/constructor.js',
	'lib/internal/console/global.js',
	'lib/internal/crypto/certificate.js',
	'lib/internal/crypto/cipher.js',
	'lib/internal/crypto/diffiehellman.js',
	'lib/internal/crypto/hash.js',
	'lib/internal/crypto/keygen.js',
	'lib/internal/crypto/keys.js',
	'lib/internal/crypto/pbkdf2.js',
	'lib/internal/crypto/random.js',
	'lib/internal/crypto/scrypt.js',
	'lib/internal/crypto/sig.js',
	'lib/internal/crypto/util.js',
	'lib/internal/constants.js',
	'lib/internal/dgram.js',
	'lib/internal/dns/promises.js',
	'lib/internal/dns/utils.js',
	'lib/internal/dtrace.js',
	'lib/internal/encoding.js',
	'lib/internal/errors.js',
	'lib/internal/error-serdes.js',
	'lib/internal/fixed_queue.js',
	'lib/internal/freelist.js',
	'lib/internal/freeze_intrinsics.js',
	'lib/internal/fs/dir.js',
	'lib/internal/fs/promises.js',
	'lib/internal/fs/read_file_context.js',
	'lib/internal/fs/rimraf.js',
	'lib/internal/fs/streams.js',
	'lib/internal/fs/sync_write_stream.js',
	'lib/internal/fs/utils.js',
	'lib/internal/fs/watchers.js',
	'lib/internal/http.js',
	'lib/internal/idna.js',
	'lib/internal/inspector_async_hook.js',
	'lib/internal/js_stream_socket.js',
	'lib/internal/linkedlist.js',
	'lib/internal/main/check_syntax.js',
	'lib/internal/main/eval_string.js',
	'lib/internal/main/eval_stdin.js',
	'lib/internal/main/inspect.js',
	'lib/internal/main/print_bash_completion.js',
	'lib/internal/main/print_help.js',
	'lib/internal/main/prof_process.js',
	'lib/internal/main/repl.js',
	'lib/internal/main/run_main_module.js',
	'lib/internal/main/run_third_party_main.js',
	'lib/internal/main/worker_thread.js',
	'lib/internal/modules/cjs/helpers.js',
	'lib/internal/modules/cjs/loader.js',
	'lib/internal/modules/esm/loader.js',
	'lib/internal/modules/esm/create_dynamic_module.js',
	'lib/internal/modules/esm/default_resolve.js',
	'lib/internal/modules/esm/module_job.js',
	'lib/internal/modules/esm/module_map.js',
	'lib/internal/modules/esm/translators.js',
	'lib/internal/net.js',
	'lib/internal/options.js',
	'lib/internal/policy/manifest.js',
	'lib/internal/policy/sri.js',
	'lib/internal/priority_queue.js',
	'lib/internal/process/esm_loader.js',
	'lib/internal/process/execution.js',
	'lib/internal/process/main_thread_only.js',
	'lib/internal/process/per_thread.js',
	'lib/internal/process/policy.js',
	'lib/internal/process/promises.js',
	'lib/internal/process/stdio.js',
	'lib/internal/process/warning.js',
	'lib/internal/process/worker_thread_only.js',
	'lib/internal/process/report.js',
	'lib/internal/process/task_queues.js',
	'lib/internal/querystring.js',
	'lib/internal/readline/utils.js',
	'lib/internal/repl.js',
	'lib/internal/repl/await.js',
	'lib/internal/repl/history.js',
	'lib/internal/repl/utils.js',
	'lib/internal/socket_list.js',
	'lib/internal/source_map/source_map.js',
	'lib/internal/source_map/source_map_cache.js',
	'lib/internal/test/binding.js',
	'lib/internal/timers.js',
	'lib/internal/tls.js',
	'lib/internal/trace_events_async_hooks.js',
	'lib/internal/tty.js',
	'lib/internal/url.js',
	'lib/internal/util.js',
	'lib/internal/util/comparisons.js',
	'lib/internal/util/debuglog.js',
	'lib/internal/util/inspect.js',
	'lib/internal/util/inspector.js',
	'lib/internal/util/types.js',
	'lib/internal/http2/core.js',
	'lib/internal/http2/compat.js',
	'lib/internal/http2/util.js',
	'lib/internal/v8_prof_polyfill.js',
	'lib/internal/v8_prof_processor.js',
	'lib/internal/validators.js',
	'lib/internal/stream_base_commons.js',
	'lib/internal/vm/source_text_module.js',
	'lib/internal/worker.js',
	'lib/internal/worker/io.js',
	'lib/internal/streams/lazy_transform.js',
	'lib/internal/streams/async_iterator.js',
	'lib/internal/streams/buffer_list.js',
	'lib/internal/streams/duplexpair.js',
	'lib/internal/streams/legacy.js',
	'lib/internal/streams/destroy.js',
	'lib/internal/streams/state.js',
	'lib/internal/streams/pipeline.js',
	'lib/internal/streams/end-of-stream.js',
	'deps/v8/tools/splaytree.js',
	'deps/v8/tools/codemap.js',
	'deps/v8/tools/consarray.js',
	'deps/v8/tools/csvparser.js',
	'deps/v8/tools/profile.js',
	'deps/v8/tools/profile_view.js',
	'deps/v8/tools/logreader.js',
	'deps/v8/tools/arguments.js',
	'deps/v8/tools/tickprocessor.js',
	'deps/v8/tools/SourceMap.js',
	'deps/v8/tools/tickprocessor-driver.js',
	'deps/node-inspect/lib/_inspect.js',
	'deps/node-inspect/lib/internal/inspect_client.js',
	'deps/node-inspect/lib/internal/inspect_repl.js',
	'deps/acorn/acorn/dist/acorn.js',
	'deps/acorn/acorn-walk/dist/walk.js',
	'deps/acorn-plugins/acorn-class-fields/index.js',
	'deps/acorn-plugins/acorn-numeric-separator/index.js',
	'deps/acorn-plugins/acorn-private-class-elements/index.js',
	'deps/acorn-plugins/acorn-private-methods/index.js',
	'deps/acorn-plugins/acorn-static-class-features/index.js',
	'lib/_third_party_main.js',
	'config.gypi',
	'tools/js2c_macros/notrace_macros.py',
	'tools/js2c_macros/nodcheck_macros.py',
	'tools/js2c_macros/dcheck_macros.py',
]

noderoot = sys.argv[1]

mtimes = []

for inFile in inputs:
	mtimes = mtimes + [ os.path.getmtime(os.path.join(noderoot, inFile)) ]

mtimes = mtimes + [ os.path.getmtime(sys.argv[0]) ]

mtimes.sort()
mtimes.reverse()

minputs = []

for inFile in inputs:
	minputs = minputs + [ inFile.replace('/', os.path.sep) ]

outFile = os.path.join(noderoot, 'src/node_javascript.cc')

if not os.path.exists(outFile) or os.path.getmtime(outFile) < mtimes[0]:
	subprocess.check_call(['python', 'tools/js2c.py'] + minputs + ['--target', 'src/node_javascript.cc'], cwd = noderoot)
