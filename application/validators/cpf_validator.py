def validate_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11
