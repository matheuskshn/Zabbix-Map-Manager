import inspect

def log(message):
    """Função auxiliar para logar mensagens com a tag da função atual."""
    caller_name = inspect.stack()[1].function.upper()
    print(f"[{caller_name}] {message}")
