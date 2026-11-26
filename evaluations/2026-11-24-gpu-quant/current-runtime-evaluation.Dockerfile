FROM sha256:97b08c5ce375113809299fc8c5dd86ae60600f618158d15fe4ad5fc9d7f4b7ae AS testdeps
FROM sha256:585c221367f9479d3962bc66c8c6f11d1ca571c9e5d7b3aa565ed02d9651b124
COPY --from=testdeps /opt/eval-test-deps/_pytest/ /opt/hermes/.venv/lib/python3.14/site-packages/_pytest/
COPY --from=testdeps /opt/eval-test-deps/pytest/ /opt/hermes/.venv/lib/python3.14/site-packages/pytest/
COPY --from=testdeps /opt/eval-test-deps/pytest-9.1.1.dist-info/ /opt/hermes/.venv/lib/python3.14/site-packages/pytest-9.1.1.dist-info/
COPY --from=testdeps /opt/eval-test-deps/iniconfig/ /opt/hermes/.venv/lib/python3.14/site-packages/iniconfig/
COPY --from=testdeps /opt/eval-test-deps/iniconfig-2.3.0.dist-info/ /opt/hermes/.venv/lib/python3.14/site-packages/iniconfig-2.3.0.dist-info/
COPY --from=testdeps /opt/eval-test-deps/pluggy/ /opt/hermes/.venv/lib/python3.14/site-packages/pluggy/
COPY --from=testdeps /opt/eval-test-deps/pluggy-1.6.0.dist-info/ /opt/hermes/.venv/lib/python3.14/site-packages/pluggy-1.6.0.dist-info/
COPY --from=testdeps /opt/eval-test-deps/py.py /opt/hermes/.venv/lib/python3.14/site-packages/py.py
COPY --from=testdeps /usr/local/bin/pytest /usr/local/bin/pytest
LABEL hermes.gpuquant.runtime="current-owner-plus-pinned-test-deps"
