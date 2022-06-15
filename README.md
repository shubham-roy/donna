# Donna
#### The best secretary that you can hope for in your PC!!

---

## Table Of Contents

* [Code Coverage](#code-coverage)
* [Setup](#setup)
* [Donna's Services](#donnas-services)
* [Developer Guidelines](#developer-guidelines)

---

## Code Coverage

<!-- Pytest Coverage Comment:Begin -->

<a href="https://github.com/shubham-roy/donna/blob/master/README.md"><img alt="Coverage" src="https://img.shields.io/badge/Coverage-93%25-brightgreen.svg" /></a><br/><details><summary>Coverage Report </summary><table><tr><th>File</th><th>Stmts</th><th>Miss</th><th>Cover</th><th>Missing</th></tr><tbody><tr><td colspan="5"><b>donna</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/shubham-roy/donna/blob/master/donna/cli.py">cli.py</a></td><td>19</td><td>5</td><td>74%</td><td><a href="https://github.com/shubham-roy/donna/blob/master/donna/cli.py#L13-L17">13&ndash;17</a></td></tr><tr><td><b>TOTAL</b></td><td><b>70</b></td><td><b>5</b></td><td><b>93%</b></td><td>&nbsp;</td></tr></tbody></table></details>

| Tests | Skipped | Failures | Errors | Time |
| ----- | ------- | -------- | -------- | ------------------ |
| 5 | 0 :zzz: | 0 :x: | 0 :fire: | 0.438s :stopwatch: |


<!-- Pytest Coverage Comment:End -->

---

## Setup

**Official Supported OS: Windows. All below-mentioned instructions are given from Windows point of view.**

May also work on Mac and Linux.

1. To get started make sure you have Python version 3.10 or above installed into your system. If not, checkout this [link](https://www.python.org/downloads/). Once installed, verify using `python --version`.
2. Have git installed into your system. If not, checkout this [link](https://git-scm.com/downloads). Once installed, verify using `git --version`.
3. Go to your preferred directory and open the terminal/powershell.
4. Execute: `git clone https://github.com/shubham-roy/donna.git`.
5. Execute: `cd donna`.
6. Execute: `pip install .`.

---

## Donna's Services

#### Screenshot

With screenshot service users can set up to take screenshots for a specified duration with a control on the interval between two successive screenshots. The following options are available for fine-grained control:

| Option     	| Alias 	| Type    	| Required 	| Default                                              	| Description                                                                                 	|
|------------	|-------	|---------	|----------	|------------------------------------------------------	|---------------------------------------------------------------------------------------------	|
| --interval 	| -i    	| Integer 	| Yes      	| -                                                    	| The gap between two consecutive screenshots in seconds.                                     	|
| --duration 	| -d    	| Integer 	| Yes      	| -                                                    	| The total duration for which to  take screenshots in minutes.                               	|
| --path     	| -p    	| String  	| No       	| A folder named `Donna` in current directory of user. 	| Full path of the folder to store the screenshots. If folder is absent, it will be created.  	|

An important usage note is not to keep `interval` more than `duration`.

Example: `donna take-ss --interval 10 --duration 1  --path <your-desired-path>`

---

## Developer Guidelines

1. After executing steps 1-6 from [Setup](#setup), execute: `pip install -r requirements_dev.txt`.
2. Before pushing a change always execute: `black ./` from the project root directory.
3. Give proper code-coverage for all your contributions and make sure that all unit-tests pass by executing `pytest` from the project root directory.
4. Always use PRs to submit new changes. **Add [shubham-roy](https://github.com/shubham-roy) as a reviewer.** Wait for [shubham-roy](https://github.com/shubham-roy) approval before merging.
5. Add proper documentation for your changes in the PR description and also update this README wherever necessary.
6. **Do not** modify anything in the [Code Coverage](#code-coverage) section of this README. It will be auto-updated by the CI workflow as and when needed.

---
