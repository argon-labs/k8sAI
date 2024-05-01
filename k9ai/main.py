# file: k9ai/main.py
"""
This module contains the commands for the CLI.
"""

import subprocess
import click

from k9ai.kuberag.main import K9ai
from k9ai.util import console


@click.group()
def chat_group():
    """
    This tool uses OpenAI's ChatGPT to chat about Kubernetes.
    It is enhanced with a retriever storing k8s documentation to improve results.
    It uses your OpenAI API key from $OPENAI_API_KEY to access the model.

    NOTE: This tool sends data to OpenAI's servers. Please review the OpenAI API terms of use.
    """


@chat_group.command()
@click.option(
    "-p", "--prompt", help="Initial prompt to start the conversation. (optional)"
)
@click.option(
    "-t",
    "--terminal",
    is_flag=True,
    default=False,
    help="If terminal is enabled, K9ai will end the conversation (optional)",
)
@click.option(
    "--disable-execution",
    is_flag=True,
    default=False,
    help="If execution is disabled, K9ai wil not \
                be capable of executing kubectl commands (optional)",
)
def chat(prompt, terminal, disable_execution):
    """
    Start a conversation with the K9ai model.
    K9ai can suggest commands that can then be executed.
    """
    kube_ai = K9ai(disable_execution)
    console.print(":robot: starting conversation with K9ai...")
    if not terminal:
        console.print("Type 'exit' to end the conversation.")

    kube_ai.start_chat(prompt, terminal=terminal)


@chat_group.command()
@click.option("--cmd", help="Kubectl command that K9ai will explain the results of")
@click.option(
    "-p",
    "--prompt",
    help="Additional prompt to go along with command output,\
                otherwise default prompt is used (optional)",
)
@click.option(
    "-t",
    "--terminal",
    is_flag=True,
    default=False,
    help="If terminal is enabled, K9ai will end the conversation (optional)",
)
@click.option(
    "--disable-execution",
    is_flag=True,
    default=False,
    help="If execution is disabled, K9ai wil not be \
                capable of executing kubectl commands (optional)",
)
def explain(cmd, prompt, terminal, disable_execution):
    """
    kubectl command will be executed and K9ai will explain the result
    """

    if not cmd.startswith("kubectl"):
        console.print("Error: Command must be kubectl command")
        return

    console.print(f":gear: running command: {cmd}")
    output = subprocess.check_output(cmd, shell=True).decode("utf-8")
    console.print(f":green_circle: command complete:\n{output}")

    if not prompt:
        prompt = "Concisely explain the output of the following command: " + cmd

    kube_ai = K9ai(disable_execution)
    console.print("Explaining kubectl results with K9ai...")
    if not terminal:
        console.print("Type 'exit' to end the conversation.")

    kube_ai.start_chat(prompt, command_output=output, terminal=terminal)


@chat_group.command()
@click.option("-p", "--prompt", help="A prompt describing the problem (optional)")
@click.option(
    "-t",
    "--terminal",
    is_flag=True,
    default=False,
    help="If terminal is enabled, K9ai will end the conversation (optional)",
)
@click.option(
    "--disable-execution",
    is_flag=True,
    default=False,
    help="If execution is disabled, K9ai wil not be capable of \
                executing kubectl commands (optional)",
)
def fix(prompt, terminal, disable_execution):
    """
    K9ai will suggest a fix based on a description of the problem
    (or try to find a problem if none is provided)
    """

    enhanced_prompt = "Look for the root cause of the problem and suggest a fix."
    if prompt:
        enhanced_prompt += "The problem is:\n" + prompt
    else:
        enhanced_prompt += "Try to find the problem with your tools, \
            follow your best instincts for troubleshooting."

    kube_ai = K9ai(disable_execution)
    console.print("Looking for fix with K9ai...")
    if not terminal:
        console.print("Type 'exit' to end the conversation.")

    kube_ai.start_chat(enhanced_prompt, terminal=terminal)


def main():
    """
    Main function for the CLI.
    """
    chat_group()