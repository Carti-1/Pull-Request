def validar_email(email:str):
    """Validação inicial simplificada (intencionalmente incompleta)."""
    if not isinstance(email, str):
        return False

    return isinstance(email, str) and "@" in email

# TODO: Implementar validação de email mais robusta, incluindo verificação de domínio e formato adequado.