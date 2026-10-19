# CloudPulse

### Lightweight Website Health & Performance Monitor

CloudPulse is a Python learning and portfolio project that checks
selected websites, records their HTTP status and response time, and
produces a readable health report. The project is being built
incrementally, with an emphasis on reusable functions, automated tests,
clear documentation, and a future CI workflow.

> **Project status:** In development. The core service-checking and
> performance-classification pieces exist; integration and verification
> are the current priorities. Automation is planned, not yet assumed to
> be configured.

------------------------------------------------------------------------

## Contents

-   [Project goals](#project-goals)
-   [How CloudPulse works](#how-cloudpulse-works)
-   [Architecture and file
    responsibilities](#architecture-and-file-responsibilities)
-   [Requirements](#requirements)
-   [Run CloudPulse](#run-cloudpulse)
-   [Run tests](#run-tests)
-   [Performance thresholds](#performance-thresholds)
-   [Development workflow](#development-workflow)
-   [Git, GitHub, and automation
    roadmap](#git-github-and-automation-roadmap)
-   [Known limitations and next
    steps](#known-limitations-and-next-steps)

## Project goals

-   Check configured websites using HTTP requests.
-   Capture HTTP status codes and measure response time.
-   Distinguish service health from response-time performance.
-   Handle unreachable services and request failures without crashing
    the whole report.
-   Keep logic in reusable modules and test important behaviour with
    `pytest`.
-   Build a clear foundation for Git-based version control and
    continuous integration.

## How CloudPulse works

The configured service list tells CloudPulse **what to check**. The
service-checking function performs the request and returns the results.
The health and performance functions interpret those results, and the
main application prints the report.

``` mermaid
flowchart TD
    A["CloudPulse.py<br/>Configured service names and URLs"] --> B["check_service(name, url)<br/>HTTP request and timing"]
    B --> C["Result dictionary<br/>status, response time, errors"]
    C --> D["check_health(status_code)<br/>Health classification"]
    C --> E["classify_performance(response_time_ms)<br/>Performance classification"]
    D --> F["CloudPulse health report"]
    E --> F
```

### What the data flow means

1.  `CloudPulse.py` holds the service names and URLs to monitor.
2.  `check_service()` sends an HTTP request and measures how long it
    takes.
3.  The function returns a dictionary containing results such as
    `status_code`, `response_time_ms`, `health`, and `performance`. For
    a failed request, some values can be `None` and an error explanation
    is returned.
4.  `check_health()` interprets the status code.
5.  `classify_performance()` interprets the measured response time.
6.  `CloudPulse.py` displays the results.

## Architecture and file responsibilities

``` mermaid
flowchart LR
    MAIN["CloudPulse.py<br/>Entry point and report"]
    MON["Service-checking module<br/>check_service()"]
    PERF["performance.py<br/>classify_performance()"]
    TESTS["pytest test modules"]
    URLS["Configured service list"]

    URLS --> MAIN
    MAIN --> MON
    MAIN --> PERF
    MON --> PERF
    TESTS -. tests .-> MON
    TESTS -. tests .-> PERF
```

> **Important:** Replace "Service-checking module" in this diagram with
> the actual filename that contains `check_service()`. The project has
> used files such as `test_response_time.py` during experimentation, but
> a file named `test_*.py` is conventionally treated as a test module by
> pytest. A future cleanup should move reusable application logic into a
> clearly named module such as `service_monitor.py`, then keep tests in
> `test_*.py` files.

### Main files

  ------------------------------------------------------------------------------
  File                                Responsibility
  ----------------------------------- ------------------------------------------
  `CloudPulse.py`                     Main application, configured services,
                                      report output, and coordination of
                                      functions.

  `performance.py`                    Reusable
                                      `classify_performance(response_time_ms)`
                                      function.

  Service-checking module             Reusable `check_service(name, url)`
                                      function that performs HTTP requests,
                                      measures response time, and handles
                                      request errors. Confirm the current
                                      filename and update this entry.

  `test_classify_performance.py`      Tests performance classifications,
                                      including missing response time.

  `test_response_time.py`             Response-time related tests or
                                      experiments; confirm its current role
                                      before treating it as a pure test file.

  `test_health_report.py`             Tests or experiments related to report
                                      behaviour.

  `test_connection_errors.py`         Tests or experiments for connection
                                      failures.

  `test_failure_types.py`             Tests or experiments for different request
                                      failure types.

  `response_time_ms.py`               Response-time experiment/helper file;
                                      confirm whether it is still needed.

  `README.md`                         Project documentation and development
                                      guide.
  ------------------------------------------------------------------------------

The file list above is a working inventory based on the current
development notes, not a verified directory listing. Update it to match
the actual Visual Studio project before publishing.

## Requirements

-   Python
-   `requests`
-   `pytest` for tests

Install dependencies in your active Python environment:

``` bash
python -m pip install requests pytest
```

Run commands from the directory containing `CloudPulse.py` and the
relevant modules. If Visual Studio uses a virtual environment, activate
or select that environment first.

## Run CloudPulse

``` bash
python CloudPulse.py
```

The program should print a report for each configured service, including
the HTTP status, response time, health, and performance where available.
A remote website may be unavailable, block requests, redirect, or
respond differently over time; results are snapshots, not a guarantee of
continuous availability.

## Run tests

Run the performance-classification tests:

``` bash
python -m pytest -v test_classify_performance.py
```

Run the full test suite:

``` bash
python -m pytest -v
```

The development record confirms that all four tests in
`test_classify_performance.py` passed at one point. Re-run tests after
code changes; do not treat a previous passing result as proof that the
current version passes.

## Performance thresholds

`performance.py` currently defines these thresholds:

  Response time                    Classification
  -------------------------------- ----------------
  Less than 500 ms                 `FAST`
  500 ms through 1000 ms           `SLOW`
  Greater than 1000 ms             `VERY SLOW`
  Missing response time (`None`)   `UNKNOWN`

These are simple project thresholds for learning and demonstration. They
are not universal service-level objectives.

## Development workflow

Use a small, repeatable cycle for each change:

1.  **Understand the change.** Identify which module owns the behaviour.
2.  **Make a small edit.** Avoid changing several unrelated files at
    once.
3.  **Run the focused test.** For example, run
    `test_classify_performance.py` after changing performance
    classification.
4.  **Run the full test suite.** Use `python -m pytest -v`.
5.  **Run the application.** Use `python CloudPulse.py` and inspect
    successful and failed checks.
6.  **Document meaningful changes.** Update this README when the
    architecture or commands change.
7.  **Commit a working checkpoint.** Once Git is configured, make a
    descriptive commit.

### Current development milestones

-   [x] Create initial service health and performance logic.
-   [x] Create `performance.py` and `classify_performance()`.
-   [x] Add four performance-classification tests.
-   [x] Implement real HTTP request and response-time measurement in the
    service-checking logic.
-   [x] Add connection-error handling in the service-checking
    experiment.
-   [ ] Finish integrating the service-checking function into
    `CloudPulse.py`.
-   [ ] Handle `None` status/response-time values consistently in the
    main report.
-   [ ] Confirm the module that owns `check_service()` has a clear,
    non-test filename.
-   [ ] Verify the current file inventory and remove or archive obsolete
    experiments only after checking them.
-   [ ] Run the full test suite and confirm the current application
    works.
-   [ ] Set up Git and create a known-good commit.
-   [ ] Publish to GitHub when the repository is ready.
-   [ ] Add GitHub Actions to run tests automatically.

## Git, GitHub, and automation roadmap

These are planned steps; they are not represented as completed until
configured and tested.

### 1. Git: keep a reliable history

After confirming the project folder and checking for existing Git
history:

``` bash
git status
```

If this folder is not already a repository, initialise it from the
project root:

``` bash
git init
```

Before committing, inspect the files that will be included:

``` bash
git status
```

Add a `.gitignore` appropriate for Python and Visual Studio, and ensure
virtual environments, cache folders, local settings, and secrets are
excluded. Then stage and commit the known-good project:

``` bash
git add README.md CloudPulse.py performance.py
git add test_*.py
git commit -m "Document CloudPulse and checkpoint current implementation"
```

Adjust the file list to include the actual service-checking module and
any other files that belong in the repository. Do not blindly stage
files if the project contains secrets or unrelated material.

### 2. GitHub: publish the repository

Once local Git history is correct:

1.  Create a GitHub repository.
2.  Review visibility and ensure no secrets or private information are
    included.
3.  Connect the local repository to the GitHub remote shown by GitHub.
4.  Push the initial branch.
5.  Confirm the README renders correctly on the repository page.

### 3. GitHub Actions: automate tests

After the tests run successfully locally and the repository is on
GitHub, add a workflow under `.github/workflows/`. The intended pipeline
is:

``` mermaid
flowchart TD
    A["Developer changes code"] --> B["Commit and push to GitHub"]
    B --> C["GitHub Actions starts"]
    C --> D["Set up Python"]
    D --> E["Install dependencies"]
    E --> F["Run pytest"]
    F --> G{"Tests pass?"}
    G -->|Yes| H["Green workflow"]
    G -->|No| I["Failed workflow; inspect logs and fix"]
```

The workflow should install the project's dependencies and run
`python -m pytest -v`. We will create and test the actual workflow only
after confirming the repository layout and test suite.

## Known limitations and next steps

-   Current monitoring is a simple HTTP check, not a full observability
    platform.
-   Response times and availability can vary due to network conditions,
    redirects, rate limits, DNS, and the target service.
-   The current health rules are intentionally simple and may need to
    account for all 2xx responses and distinguish HTTP errors from
    unreachable services.
-   The current file layout needs to be verified, especially the
    filename containing `check_service()`.
-   Automated testing, GitHub publishing, and CI are planned next steps.

**Immediate next milestone:** stabilise the module layout, complete
integration in `CloudPulse.py`, run the tests, and then create the first
reliable Git checkpoint before adding automation.
