# KubeAI

KubeAI is a RAG-enabled GPT that uses a vector store with the embeddings of the [Kubernetes documentation](https://kubernetes.io/docs/).
It can answer general questions about Kubernetes, explain or suggest fixes based on the output of kubectl commands, and provide suggested commands for you to then easily execute.

### Note:
This tool sends data to OpenAI's servers. Please review the OpenAI API terms of use before using this tool.
This tool also executes `kubectl` commands. While they should be read-only commands, unintended consequences are possible. Use the `--disable-execution` command if you want to be extra-safe.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install KubeAI.

```bash
pip install <TODO>
```

### Configuration

Before using KubeAI, ensure your OpenAI API key is set as an environment variable:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

## Usage
### Chat
To start a conversation with KubeAI:
```bash
kubeai chat [OPTIONS]
```

Options:
- -p, --prompt Provide an initial prompt to start the conversation (optional)
- -t, --terminal End the conversation by closing the terminal session (optional)
- --disable-execution Disable execution of kubectl commands (optional)

### Explain
To have KubeAI explain the output of a Kubernetes command:
```bash
kubeai explain --cmd='kubectl [command]' [OPTIONS]
```

Options:
- -p, --prompt Provide an additional prompt to go along with the command output (optional)
- -t, --terminal End the conversation by closing the terminal session (optional)
- --disable-execution Disable execution of kubectl commands (optional)

Note: Only `kubectl` commands are valid for explanation.

### Fix
To request KubeAI to suggest a fix based on a provided description of the problem:
```bash
kubeai fix [OPTIONS]
```
If no prompt is provided, KubeAI will attempt to discover the problem itself (under development)

Options:
- -p, --prompt A prompt describing the problem to analyze (optional)
- -t, --terminal End the conversation by closing the terminal session (optional)
- --disable-execution Disable execution of kubectl commands (optional)

### Common Commands
```bash
# Start a chat session with KubeAI
kubeai chat

# Explain the output a specific kubectl command
kubeai explain --cmd 'kubectl get pods'

# Suggest a fix for a described problem
kubeai fix --prompt 'Pods are crashing frequently'
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

<TODO>