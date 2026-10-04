
# Do not edit *_sync.py files
The pystudershared library provides both an async as well as a sync Api.
To maintain development consistency the sync api is auto generated from the async api.
Therefore, do NOT edit the *_sync.py files.

To re-generate the sync api after editing of the async api or unit-tests:
- Open a command prompt at the root of this project
- (first time) Run: pip install unasyncd  (or: python -m pip install unasyncd)
- Run: unasyncd
