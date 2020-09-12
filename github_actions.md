CI includes more than

- fetching code
- running test 
- sshing into remote server instance
- deploying code/binary on remote server

These are actions (haha) on GitHub Actions. Terms:

- [workflow](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions): The flow executed by the CI tool when it starts.
- [job]: A workflow consists one or more jobs. It refers to the tasks in one workflow execution.
- [step]: A job consists of one or more steps which executes one by one
- [action]: Each step consists of one or more actions. The smallest execution unit.


[reference](https://www.pixelstech.net/article/1577096152-A-tutorial-on-Github-Actions)
