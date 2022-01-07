# GitHub_Actions_introduction
I thought of making this repository just for people who are new to github actions, and want to get a quick flavour of the GitHub actions.

I personally think that GitHub actions are great and makes CI/CD for open source really easy to use. So Kudos to GitHub ! :+1:

## Detailed explanation of the repository workflow
We would be basically diving deep into the yml workflow file of our repository [workflow_file](https://github.com/Vibaswan/Gihub_Actions_introduction/blob/main/.github/workflows/test.yml)

So, Lets start!

```yml
name: CI
```
we start the workflow specifying the name of the CI/CD workflow we want

```yml
on:
  push:
    branches:
      main
    paths-ignore:
      - '**/README.md'
  repository_dispatch:
  pull_request:
```

the `on:` keyword basically tells us when this particular workflow will be triggered in other words which events will trigger the actions.
we can see here `push and pull_request` are the events on which the workflow will be triggered.

For manual trigger we use `workflow_dispatch:` for example:
```yml
 inputs:
        Name:
          description: 'Name you is triggering'
          required: true
          default: 'Admin'
        purpose:
          description: 'purpose for the build trigger'
          required: true
          default: 'check'
```
in workflow dispatch the `inputs` lets you provide some arguments with which you can fire the actions. Each input then has attributes like `description, required (whether its mandatory or not), deafult`.

To know about `repository_dispatch` please go to my another repository [repository_dispatch_repo](https://github.com/Vibaswan/trigger_repo) just to give you a brief its basically used to handle dependencies.

Now in each of the events you can provide `branches` option regarding for which branch the workflow will be triggered and also `paths-ignore:` which will ignore firing the actions if those files are changed.

```yml
jobs:
  # This workflow contains a single job called "build"
  deploy_and_test:
    # The type of runner that the job will run on
    runs-on: windows-latest
    strategy:
      matrix:
        python-version: [27, 38]
```

`jobs` basically is the part where we actually start configuring our environment and start writing the script for our Ci/CD pipeline.
we can have multiple jobs in a single workflow and all the jobs are run parallely by default provided you are using runners provided by Github
In this workflow we have a single job whose name is `deploy_and_test`.

`runs-on` basically tells you in which os you want to run your workflow in, Here we are using the `windows-latest` you can also use `ubuntu-latest`.

These runners are provided by GitHub itself to know more about runner click on the link [GitHub hosted  runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners)

`strategy` basically helps us to build us different `test matrix` for our worklow. In this workflow we have matrix where we are using both versions of python.

```yml
  steps:

    # checking out my code
    - name: Checkout
      uses: actions/checkout@v2

    # basically just getting the version number for which the build got triggered
    - name: Get version number
      id: get_version
      run: echo "::set-output name=version::$(cat VERSION)"
```
Each job has a list of steps which are executed sequentially. Now inside steps we do the tasts we wan tto perform for the job.
`uses` is used if you are using a tast which is already supported by GitHub and you are just using the for you benefit, there are a lot of awesome actions which you can find in the [Github Action Marketplace](https://github.com/marketplace?type=actions).
 
You can also write you own steps and use `run` attribute the run the command you want, for multiple commands we use `run: |`.

You can even check and condition and skip a step or task with `if:`. Please see the below sample:
```yml
name: check which files changed
if: github.event_name == 'push'
uses: jitterbit/get-changed-files@v1
id: change
with:
  format: space-delimited
  token: ${{ secrets.GITHUB_TOKEN }}
```

I have some added some basic samples in the folder [GitHub Action Samples](https://github.com/Vibaswan/Gihub_Actions_introduction/tree/main/Github_action_samples).
Have a look it will help you understand more.

## Hope this helped you !! :sparkles::sparkles:
