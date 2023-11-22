EVA_SUCCESS_CODES = {
    "00": {
        "description": "Entrada veículo na pista",
        "action": "Ação1",
    },
    "01": {
        "description": "Leitura de TAG identificada",
        "action": "Ação1",
    },
    "SA": {
        "description": "Solicitação de Autorização",
        "action": "Ação2",
    },
    "03": {
        "description": "Imagem de placa capturada",
        "action": "Ação3",
    },
    "05": {
        "description": "Cliente aprovado On-line",
        "action": "Ação4",
    },
    "09": {
        "description": "Match de placa",
        "action": "Ação5",
    },
    "30": {
        "description": "Recuperação do sensor de presença",
        "action": "Ação6",
    },
    "31": {
        "description": "TAG OK na contingência do sensor",
        "action": "Ação7",
    },
    "38": {
        "description": "Match de placa NOK na contingência do sensor",
        "action": "Ação8",
    },
    "39": {
        "description": "Match de placa OK na contingência do sensor",
        "action": "Ação9",
    },
    "50": {
        "description": "Bico retirado",
        "action": "Ação10",
    },
    "51": {
        "description": "Final do fluxo",
        "action": "Ação11",
    },
    "52": {
        "description": "Bico reinserido",
        "action": "Ação12",
    },
    "53": {
        "description": "Entrega do pacote de abastecimento",
        "action": "Ação13",
    },
    "54": {
        "description": "Desocupação do sensor de presença",
        "action": "Ação14",
    },
}

EVA_ERROR_CODES = {
    "02": {
        "description": "Imagem da placa não capturada",
        "action": "Ação15",
    },
    "04": {
        "description": "Cliente reprovado Online",
        "action": "Ação16",
    },
    "06": {
        "description": "Cliente reprovado Off-line (contingência)/Timeout da fachada",
        "action": "Ação17",
    },
    "07": {
        "description": "Cliente aprovado Off-line (contingência)",
        "action": "Ação18",
    },
    "08": {
        "description": "Match de placa",
        "action": "Ação19",
    },
    "99": {
        "description": "Cancelamento do pagamento via Sem Parar",
        "action": "Ação20",
    },
}

PAYMENT_CANCEL_SUB_ERRORS = {
    "0": {
        "description": "PagamentoDoAbastecimentoCanceladoViaCartão/BotãoDeCancelamento",
        "action": "Ação21",
    },
    "1": {
        "description": "Time out para recebimento do evento de abastecimento",
        "action": "Ação22",
    },
    "2": {
        "description": "Limite do volume foi excedido",
        "action": "Ação23",
    },
    "3": {
        "description": "Limite de valor foi excedido",
        "action": "Ação24",
    },
    "4": {
        "description": "Bomba NOK, ou bico fora do handler",
        "action": "Ação25",
    },
    "5": {
        "description": "Timeout da resposta da fachada 'reserva transação'",
        "action": "Ação26",
    },
    "6": {
        "description": "Retirada de bico sem sensor",
        "action": "Ação27",
    },
    "7": {
        "description": "Retorno de bico sem sensor",
        "action": "Ação28",
    },
    "8": {
        "description": "Cancelado por saída de veiculo",
        "action": "Ação29",
    },
    "9": {
        "description": "Time out para início do abastecimento",
        "action": "Ação30",
    },
    "10": {
        "description": "Transação negada pela GetNet",
        "action": "Ação31",
    },
    "11": {
        "description": "Bico reinserido sem fluxo de combustível",
        "action": "Ação32",
    },
}
