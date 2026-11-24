---
title: "Política de privacidade"
lang: pt-BR
permalink: /privacy/pt-BR/
---

# Política de privacidade do Ætherna

_Última atualização: 24 de novembro de 2026_

O Ætherna é um app para ouvir conversas em áudio sobre obras. Esta política explica o que o app e o servidor do Ætherna guardam, e por quê.

## O que coletamos

- **Identificador da sua conta Apple.** Ao entrar com a Apple, recebemos um identificador anônimo que a Apple cria para este app. Guardamos só uma impressão cifrada (HMAC) dele, para reconhecer a sua conta. **Não pedimos nem guardamos seu nome nem seu e-mail.**
- **Sessão do aparelho.** Um código de sessão fica no Keychain do aparelho; no servidor guardamos só a impressão (SHA-256) dele.
- **Assinatura.** Se você assina o Premium, guardamos o produto, o ambiente da compra, a data de vencimento e uma impressão cifrada do número da transação da Apple, para liberar os recursos pagos. **Não recebemos dados de cartão nem de pagamento:** quem cobra é a Apple.
- **Episódio em andamento.** No plano grátis, o servidor lembra qual episódio você está ouvindo agora, para aplicar a regra de um episódio por vez.

## O que não coletamos

O app não tem anúncios, não usa SDK de análise ou rastreamento e não vende nem compartilha dados com terceiros para publicidade. Seu histórico de escuta, posições e preferências ficam **no aparelho**.

## Dados no aparelho

O token de sessão fica no Keychain, só neste aparelho. Episódios baixados ficam no armazenamento do app, fora do backup. Posições de reprodução e preferências ficam no armazenamento do app. Apagar o app apaga esses dados do aparelho.

## Rede e provedores

O app fala com o servidor do Ætherna por HTTPS, através da Cloudflare, que processa o endereço IP das conexões para entregar o tráfego e proteger o serviço. O servidor usa o endereço IP por alguns minutos, só na memória, para limitar abusos no cadastro.

## Apagar sua conta

Em Ajustes → Conta → **Excluir minha conta**, o app apaga no servidor a sua conta, as sessões, a assinatura registrada e o episódio em andamento. Para cancelar a cobrança da assinatura, cancele também nos Ajustes da sua conta Apple.

## Crianças

O Ætherna não é dirigido a menores de 13 anos e não coleta dados de crianças de propósito.

## Contato e mudanças

Dúvidas sobre privacidade: abra uma issue em https://github.com/JoaoZaokk/aetherna-app/issues. Mudanças nesta política aparecem nesta página, com a data no topo.
