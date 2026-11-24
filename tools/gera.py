"""Gera as páginas públicas do Ætherna (README, privacidade, termos) nas 5 línguas.

As mesmas frases alimentam a ficha da App Store (tools/loja.json). Rodar:
    python3 tools/gera.py
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
REPO = "https://github.com/JoaoZaokk/aetherna-app"
SITE = "https://joaozaokk.github.io/aetherna-app"
EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"
DATA = {"pt-BR": "24 de novembro de 2026", "en": "November 24, 2026", "de": "24. November 2026",
        "zh-Hant": "2026 年 11 月 24 日", "zh-Hans": "2026 年 11 月 24 日"}
NOMES = {"pt-BR": "Português (Brasil)", "en": "English", "de": "Deutsch",
         "zh-Hant": "繁體中文（台灣）", "zh-Hans": "简体中文"}

T = {}

T["pt-BR"] = dict(
    subtitulo="Conversas em áudio sobre obras",
    promo="Livros, filmes, séries, animes e história em conversas de áudio: mergulhos guiados e debates para ouvir onde quiser.",
    palavras="podcast,áudio,livros,filmes,séries,anime,mangá,história,debate,resumo,análise,cinema,ia,ouvir",
    descricao="""O Ætherna transforma livros, filmes, séries, animes e grandes temas da história em conversas em áudio para você ouvir onde quiser.

Cada obra ganha dois formatos:
• Deep dive: um mergulho guiado, parte por parte, no enredo, nos personagens e no contexto.
• Debate: duas vozes discutindo as ideias, os acertos e as polêmicas da obra.

O QUE VOCÊ ENCONTRA
• Centenas de obras e mais de mil episódios, por categoria: cinema, séries, história, mistérios, crimes, anime e mangá, games e mais.
• Séries agrupadas: anime e mangá, temporadas e partes numa tela só.
• Ordem sem spoiler: o app segue a ordem da obra e avisa quando um episódio está à frente de onde você parou.
• Player completo: velocidade, voltar 15 s e avançar 30 s, timer de sono e controles na tela bloqueada.
• Quatro estilos visuais: Cinemateca, Edição, Sinal e Vidro.
• Interface e catálogo em português, inglês e alemão.

ÆTHERNA PREMIUM
No plano grátis você ouve um episódio por vez. Com o Premium você:
• baixa episódios para ouvir sem internet;
• lê o texto da conversa acompanhando o áudio;
• ouve quantos episódios quiser, sem esperar.

TRANSPARÊNCIA
As conversas são geradas por inteligência artificial e narradas por vozes sintéticas, e cada episódio mostra esses selos. Os episódios são comentários e análises sobre as obras, não a leitura delas. O Ætherna não tem vínculo com autores, editoras ou estúdios.

ASSINATURA
O Ætherna Premium é uma assinatura mensal com renovação automática. O valor é cobrado na sua conta Apple quando você confirma a compra. A assinatura renova sozinha, a menos que seja cancelada pelo menos 24 horas antes do fim do período atual. Gerencie ou cancele nos Ajustes da sua conta Apple.""",
    termos_rotulo="Termos de uso", priv_rotulo="Política de privacidade", suporte_rotulo="Suporte",
    novidades_rotulo="Novidades",
    readme_intro="Conversas em áudio, geradas por IA, sobre livros, filmes, séries, animes e história. Este repositório não tem o código do app: serve para avisos de atualização, suporte e os documentos legais.",
    suporte="Encontrou um problema ou quer sugerir algo? Abra uma issue: {repo}/issues/new/choose. Não coloque dados pessoais na issue: ela é pública.",
    priv="""# Política de privacidade do Ætherna

_Última atualização: {data}_

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

Dúvidas sobre privacidade: abra uma issue em {repo}/issues. Mudanças nesta política aparecem nesta página, com a data no topo.
""",
    termos="""# Termos de uso do Ætherna

_Última atualização: {data}_

O uso do Ætherna segue o **Contrato de Licença de Usuário Final padrão da Apple** ({eula}), com os pontos abaixo.

## O conteúdo

Os episódios são **conversas geradas por inteligência artificial** e narradas por **vozes sintéticas**. São comentários, análises e debates sobre obras e temas, não a leitura das obras, e podem conter erros. O Ætherna não tem vínculo com autores, editoras, estúdios nem detentores de direitos das obras comentadas. Os episódios são para uso pessoal: não redistribua.

## Ætherna Premium

- Assinatura mensal com renovação automática, comprada pela App Store.
- O valor é cobrado na sua conta Apple quando você confirma a compra.
- A renovação é automática, a menos que você cancele pelo menos 24 horas antes do fim do período atual. A cobrança da renovação acontece nas 24 horas antes do fim do período.
- Você gerencia e cancela a assinatura nos Ajustes da sua conta Apple. Reembolsos seguem as regras da Apple.

## Plano grátis

No plano grátis você ouve um episódio por vez, sem baixar episódios e sem o texto sincronizado. Os limites podem mudar com aviso no app ou nesta página.

## Conta

A conta usa o Entrar com a Apple. Você pode excluir a conta a qualquer momento em Ajustes → Conta.

## Contato

Abra uma issue em {repo}/issues.
""",
    changelog="""# Novidades

## 1.0
- Primeira versão: deep dives e debates em áudio, catálogo por categoria, séries agrupadas (anime e mangá, temporadas), ordem sem spoiler, quatro estilos visuais e três idiomas.
- Ætherna Premium: baixar episódios, texto sincronizado e vários episódios ao mesmo tempo.
""",
)

T["en"] = dict(
    subtitulo="Audio deep dives and debates",
    promo="Books, films, series, anime and history as audio conversations: guided deep dives and debates to listen to anywhere.",
    palavras="podcast,audio,books,movies,series,anime,manga,history,debate,summary,analysis,film,ai,listen",
    descricao="""Ætherna turns books, films, TV series, anime and the great themes of history into audio conversations you can listen to anywhere.

Every work comes in two formats:
• Deep dive: a guided journey, part by part, through the plot, the characters and the context.
• Debate: two voices discussing the ideas, the highlights and the controversies of the work.

WHAT YOU GET
• Hundreds of works and over a thousand episodes, by category: film, series, history, mysteries, true crime, anime and manga, games and more.
• Grouped series: anime and manga, seasons and parts on a single screen.
• Spoiler-free order: the app follows the work's order and warns you when an episode is ahead of where you stopped.
• A complete player: speed, skip back 15 s and forward 30 s, sleep timer and lock screen controls.
• Four visual styles: Cinematheque, Edition, Signal and Glass.
• Interface and catalog in Portuguese, English and German.

ÆTHERNA PREMIUM
On the free plan you listen to one episode at a time. With Premium you:
• download episodes to listen offline;
• read the conversation's text as the audio plays;
• listen to as many episodes as you like, without waiting.

TRANSPARENCY
The conversations are generated by artificial intelligence and narrated by synthetic voices, and every episode shows these labels. Episodes are commentary and analysis about the works, not readings of them. Ætherna is not affiliated with any author, publisher or studio.

SUBSCRIPTION
Ætherna Premium is a monthly auto-renewing subscription. Payment is charged to your Apple Account when you confirm the purchase. The subscription renews automatically unless it is cancelled at least 24 hours before the end of the current period. Manage or cancel it in your Apple Account settings.""",
    termos_rotulo="Terms of Use", priv_rotulo="Privacy Policy", suporte_rotulo="Support",
    novidades_rotulo="What's new",
    readme_intro="AI-generated audio conversations about books, films, series, anime and history. This repository does not hold the app's code: it is for update notes, support and the legal documents.",
    suporte="Found a problem or have a suggestion? Open an issue: {repo}/issues/new/choose. Do not put personal data in the issue: it is public.",
    priv="""# Ætherna Privacy Policy

_Last updated: {data}_

Ætherna is an app for listening to audio conversations about works. This policy explains what the app and the Ætherna server keep, and why.

## What we collect

- **Your Apple Account identifier.** When you sign in with Apple, we receive an anonymous identifier that Apple creates for this app. We keep only a keyed hash (HMAC) of it, to recognize your account. **We do not ask for or keep your name or email address.**
- **Device session.** A session code is stored in the device's Keychain; on the server we keep only its hash (SHA-256).
- **Subscription.** If you subscribe to Premium, we keep the product, the purchase environment, the expiry date and a keyed hash of Apple's transaction number, to unlock the paid features. **We never receive card or payment details:** Apple handles billing.
- **Episode in progress.** On the free plan, the server remembers which episode you are listening to right now, to apply the one-episode-at-a-time rule.

## What we do not collect

The app has no ads, uses no analytics or tracking SDKs, and does not sell or share data with third parties for advertising. Your listening history, positions and preferences stay **on the device**.

## Data on the device

The session token stays in the Keychain, on this device only. Downloaded episodes stay in the app's storage, excluded from backups. Playback positions and preferences stay in the app's storage. Deleting the app deletes this data from the device.

## Network and providers

The app talks to the Ætherna server over HTTPS through Cloudflare, which processes connection IP addresses to deliver traffic and protect the service. The server uses the IP address for a few minutes, in memory only, to limit sign-up abuse.

## Deleting your account

In Settings → Account → **Delete my account**, the app deletes from the server your account, sessions, recorded subscription and episode in progress. To stop subscription charges, also cancel in your Apple Account settings.

## Children

Ætherna is not directed at children under 13 and does not knowingly collect data from children.

## Contact and changes

Privacy questions: open an issue at {repo}/issues. Changes to this policy appear on this page, with the date at the top.
""",
    termos="""# Ætherna Terms of Use

_Last updated: {data}_

Use of Ætherna is governed by **Apple's standard Licensed Application End User License Agreement** ({eula}), together with the points below.

## The content

Episodes are **conversations generated by artificial intelligence** and narrated by **synthetic voices**. They are commentary, analysis and debate about works and topics, not readings of the works, and they may contain mistakes. Ætherna is not affiliated with the authors, publishers, studios or rights holders of the works discussed. Episodes are for personal use: do not redistribute them.

## Ætherna Premium

- Monthly auto-renewing subscription, purchased through the App Store.
- Payment is charged to your Apple Account when you confirm the purchase.
- It renews automatically unless you cancel at least 24 hours before the end of the current period. The renewal is charged within the 24 hours before the period ends.
- Manage and cancel the subscription in your Apple Account settings. Refunds follow Apple's rules.

## Free plan

On the free plan you listen to one episode at a time, without downloads and without the synchronized text. Limits may change with notice in the app or on this page.

## Account

The account uses Sign in with Apple. You can delete it at any time in Settings → Account.

## Contact

Open an issue at {repo}/issues.
""",
    changelog="""# What's new

## 1.0
- First release: audio deep dives and debates, catalog by category, grouped series (anime and manga, seasons), spoiler-free order, four visual styles and three languages.
- Ætherna Premium: downloads, synchronized text and several episodes at once.
""",
)

T["de"] = dict(
    subtitulo="Audio-Analysen und Debatten",
    promo="Bücher, Filme, Serien, Anime und Geschichte als Audiogespräche: geführte Analysen und Debatten zum Hören überall.",
    palavras="podcast,audio,bücher,filme,serien,anime,manga,geschichte,debatte,zusammenfassung,analyse,ki,hören",
    descricao="""Ætherna verwandelt Bücher, Filme, Serien, Anime und die großen Themen der Geschichte in Audiogespräche, die du überall hören kannst.

Jedes Werk gibt es in zwei Formaten:
• Deep Dive: eine geführte Reise, Teil für Teil, durch Handlung, Figuren und Hintergrund.
• Debatte: zwei Stimmen diskutieren die Ideen, Stärken und Kontroversen des Werks.

WAS DICH ERWARTET
• Hunderte Werke und über tausend Folgen, nach Kategorien: Film, Serien, Geschichte, Mysterien, True Crime, Anime und Manga, Games und mehr.
• Gruppierte Reihen: Anime und Manga, Staffeln und Teile auf einem Bildschirm.
• Reihenfolge ohne Spoiler: Die App folgt der Reihenfolge des Werks und warnt dich, wenn eine Folge weiter ist als deine Stelle.
• Vollständiger Player: Geschwindigkeit, 15 s zurück und 30 s vor, Schlaftimer und Steuerung auf dem Sperrbildschirm.
• Vier Designs: Kinemathek, Ausgabe, Signal und Glas.
• Oberfläche und Katalog auf Portugiesisch, Englisch und Deutsch.

ÆTHERNA PREMIUM
Im kostenlosen Tarif hörst du eine Folge nach der anderen. Mit Premium kannst du:
• Folgen herunterladen und offline hören;
• den Text des Gesprächs mitlesen, während der Ton läuft;
• so viele Folgen hören, wie du willst, ohne zu warten.

TRANSPARENZ
Die Gespräche werden von künstlicher Intelligenz erzeugt und von synthetischen Stimmen gesprochen; jede Folge zeigt diese Kennzeichnung. Die Folgen sind Kommentare und Analysen zu den Werken, keine Lesungen. Ætherna steht in keiner Verbindung zu Autoren, Verlagen oder Studios.

ABONNEMENT
Ætherna Premium ist ein monatliches, sich automatisch verlängerndes Abonnement. Die Zahlung wird bei Bestätigung des Kaufs deinem Apple Account belastet. Das Abo verlängert sich automatisch, sofern es nicht mindestens 24 Stunden vor Ende des laufenden Zeitraums gekündigt wird. Verwalten oder kündigen kannst du es in den Einstellungen deines Apple Accounts.""",
    termos_rotulo="Nutzungsbedingungen", priv_rotulo="Datenschutzerklärung", suporte_rotulo="Support",
    novidades_rotulo="Neuigkeiten",
    readme_intro="KI-generierte Audiogespräche über Bücher, Filme, Serien, Anime und Geschichte. Dieses Repository enthält nicht den Code der App: Es dient für Update-Hinweise, Support und die rechtlichen Dokumente.",
    suporte="Ein Problem gefunden oder eine Idee? Eröffne ein Issue: {repo}/issues/new/choose. Bitte keine persönlichen Daten ins Issue schreiben: Es ist öffentlich.",
    priv="""# Datenschutzerklärung von Ætherna

_Zuletzt aktualisiert: {data}_

Ætherna ist eine App zum Hören von Audiogesprächen über Werke. Diese Erklärung beschreibt, was die App und der Ætherna-Server speichern und warum.

## Was wir erheben

- **Kennung deines Apple Accounts.** Wenn du dich mit Apple anmeldest, erhalten wir eine anonyme Kennung, die Apple für diese App erstellt. Wir speichern nur einen verschlüsselten Hash (HMAC) davon, um dein Konto zu erkennen. **Wir fragen weder nach deinem Namen noch nach deiner E-Mail-Adresse und speichern sie nicht.**
- **Gerätesitzung.** Ein Sitzungscode liegt im Schlüsselbund des Geräts; auf dem Server speichern wir nur seinen Hash (SHA-256).
- **Abonnement.** Wenn du Premium abonnierst, speichern wir das Produkt, die Kaufumgebung, das Ablaufdatum und einen verschlüsselten Hash der Apple-Transaktionsnummer, um die bezahlten Funktionen freizuschalten. **Karten- oder Zahlungsdaten erhalten wir nie:** Die Abrechnung übernimmt Apple.
- **Laufende Folge.** Im kostenlosen Tarif merkt sich der Server, welche Folge du gerade hörst, um die Regel „eine Folge nach der anderen“ anzuwenden.

## Was wir nicht erheben

Die App hat keine Werbung, nutzt keine Analyse- oder Tracking-SDKs und verkauft oder teilt keine Daten mit Dritten zu Werbezwecken. Hörverlauf, Positionen und Einstellungen bleiben **auf dem Gerät**.

## Daten auf dem Gerät

Das Sitzungstoken bleibt im Schlüsselbund, nur auf diesem Gerät. Heruntergeladene Folgen liegen im Speicher der App, ausgenommen von Backups. Wiedergabepositionen und Einstellungen liegen im Speicher der App. Wenn du die App löschst, werden diese Daten vom Gerät entfernt.

## Netzwerk und Dienstleister

Die App kommuniziert mit dem Ætherna-Server über HTTPS via Cloudflare, das die IP-Adressen der Verbindungen verarbeitet, um den Datenverkehr zuzustellen und den Dienst zu schützen. Der Server nutzt die IP-Adresse wenige Minuten lang, nur im Arbeitsspeicher, um Missbrauch bei der Registrierung zu begrenzen.

## Konto löschen

Unter Einstellungen → Konto → **Mein Konto löschen** löscht die App auf dem Server dein Konto, deine Sitzungen, das gespeicherte Abonnement und die laufende Folge. Um Abbuchungen zu beenden, kündige das Abo zusätzlich in den Einstellungen deines Apple Accounts.

## Kinder

Ætherna richtet sich nicht an Kinder unter 13 Jahren und erhebt nicht wissentlich Daten von Kindern.

## Kontakt und Änderungen

Fragen zum Datenschutz: Eröffne ein Issue unter {repo}/issues. Änderungen dieser Erklärung erscheinen auf dieser Seite, mit dem Datum oben.
""",
    termos="""# Nutzungsbedingungen von Ætherna

_Zuletzt aktualisiert: {data}_

Für die Nutzung von Ætherna gilt der **Standard-Endbenutzer-Lizenzvertrag von Apple** ({eula}), ergänzt um die folgenden Punkte.

## Die Inhalte

Die Folgen sind **von künstlicher Intelligenz erzeugte Gespräche**, gesprochen von **synthetischen Stimmen**. Sie sind Kommentare, Analysen und Debatten über Werke und Themen, keine Lesungen der Werke, und können Fehler enthalten. Ætherna steht in keiner Verbindung zu Autoren, Verlagen, Studios oder Rechteinhabern der besprochenen Werke. Die Folgen sind für den persönlichen Gebrauch: bitte nicht weiterverbreiten.

## Ætherna Premium

- Monatliches, sich automatisch verlängerndes Abonnement, gekauft über den App Store.
- Die Zahlung wird bei Bestätigung des Kaufs deinem Apple Account belastet.
- Das Abo verlängert sich automatisch, sofern du nicht mindestens 24 Stunden vor Ende des laufenden Zeitraums kündigst. Die Verlängerung wird innerhalb der 24 Stunden vor Ende des Zeitraums berechnet.
- Verwalten und kündigen kannst du das Abo in den Einstellungen deines Apple Accounts. Erstattungen richten sich nach den Regeln von Apple.

## Kostenloser Tarif

Im kostenlosen Tarif hörst du eine Folge nach der anderen, ohne Downloads und ohne synchronisierten Text. Die Grenzen können sich mit Hinweis in der App oder auf dieser Seite ändern.

## Konto

Das Konto nutzt „Mit Apple anmelden“. Du kannst es jederzeit unter Einstellungen → Konto löschen.

## Kontakt

Eröffne ein Issue unter {repo}/issues.
""",
    changelog="""# Neuigkeiten

## 1.0
- Erste Version: Audio-Deep-Dives und Debatten, Katalog nach Kategorien, gruppierte Reihen (Anime und Manga, Staffeln), Reihenfolge ohne Spoiler, vier Designs und drei Sprachen.
- Ætherna Premium: Downloads, synchronisierter Text und mehrere Folgen gleichzeitig.
""",
)

T["zh-Hant"] = dict(
    subtitulo="作品深度解析與辯論音訊",
    promo="把書籍、電影、影集、動畫與歷史變成音訊對談：導覽式深度解析與辯論，隨時隨地收聽。",
    palavras="播客,有聲,音訊,書籍,電影,影集,動畫,漫畫,歷史,辯論,解析,摘要,AI,收聽",
    descricao="""Ætherna 把書籍、電影、影集、動畫和歷史上的重大主題，變成可以隨時隨地收聽的音訊對談。

每部作品都有兩種形式：
• 深度解析：逐段導覽劇情、角色與背景。
• 辯論：兩個聲音討論作品的想法、亮點與爭議。

內容特色
• 數百部作品、上千集節目，依類別整理：電影、影集、歷史、懸疑、犯罪、動畫與漫畫、遊戲等。
• 系列整合：動畫與漫畫、各季與各部分，集中在同一個畫面。
• 無劇透順序：依照作品的順序播放，若某集超前你目前的進度會提醒你。
• 完整播放器：播放速度、倒退 15 秒與快轉 30 秒、睡眠定時器及鎖定畫面控制。
• 四種視覺風格：電影資料館、版本、訊號與玻璃。
• 介面支援葡萄牙文、英文、德文與中文（繁體及簡體）。

ÆTHERNA PREMIUM
免費方案一次可收聽一集。升級 Premium 後你可以：
• 下載節目，離線收聽；
• 一邊播放一邊閱讀對談文字；
• 想聽幾集就聽幾集，不必等待。

透明說明
對談內容由人工智慧生成，並由合成語音朗讀，每一集都會標示。節目是對作品的評論與分析，並非作品朗讀。Ætherna 與任何作者、出版社或製作公司均無關聯。

訂閱說明
Ætherna Premium 為按月自動續訂的訂閱。確認購買時會向你的 Apple 帳號收費。除非在目前期間結束前至少 24 小時取消，否則訂閱會自動續訂。你可以在 Apple 帳號設定中管理或取消訂閱。""",
    termos_rotulo="使用條款", priv_rotulo="隱私權政策", suporte_rotulo="支援",
    novidades_rotulo="新功能",
    readme_intro="由 AI 生成、關於書籍、電影、影集、動畫與歷史的音訊對談。此儲存庫不包含 App 程式碼，僅用於更新公告、支援與法律文件。",
    suporte="發現問題或有建議嗎？請開 issue：{repo}/issues/new/choose。issue 是公開的，請勿填寫個人資料。",
    priv="""# Ætherna 隱私權政策

_最後更新：{data}_

Ætherna 是一款收聽作品相關音訊對談的 App。本政策說明 App 與 Ætherna 伺服器會保存哪些資料，以及原因。

## 我們收集的資料

- **Apple 帳號識別碼。** 使用 Apple 登入時，我們會收到 Apple 為此 App 建立的匿名識別碼。我們只保存其加密雜湊值（HMAC），用來辨識你的帳號。**我們不會要求或保存你的姓名或電子郵件。**
- **裝置工作階段。** 工作階段代碼存放在裝置的鑰匙圈中；伺服器只保存其雜湊值（SHA-256）。
- **訂閱。** 若你訂閱 Premium，我們會保存產品、購買環境、到期日，以及 Apple 交易編號的加密雜湊值，以開放付費功能。**我們不會收到任何信用卡或付款資料**，收費由 Apple 處理。
- **正在收聽的節目。** 在免費方案中，伺服器會記住你目前正在收聽的那一集，以執行「一次一集」的規則。

## 我們不收集的資料

App 沒有廣告，不使用任何分析或追蹤 SDK，也不會為了廣告而出售或與第三方分享資料。你的收聽紀錄、播放位置與偏好設定都保留**在裝置上**。

## 裝置上的資料

工作階段權杖只存放在此裝置的鑰匙圈中。下載的節目存放在 App 的儲存空間，不納入備份。播放位置與偏好設定存放在 App 的儲存空間。刪除 App 會一併刪除裝置上的這些資料。

## 網路與服務供應商

App 透過 HTTPS、經由 Cloudflare 與 Ætherna 伺服器連線；Cloudflare 會處理連線的 IP 位址以傳送流量並保護服務。伺服器只會在記憶體中短暫使用 IP 位址幾分鐘，以限制註冊濫用。

## 刪除帳號

在「設定 → 帳號 → **刪除我的帳號**」中，App 會從伺服器刪除你的帳號、工作階段、已記錄的訂閱及正在收聽的節目。若要停止訂閱收費，請同時在 Apple 帳號設定中取消訂閱。

## 兒童

Ætherna 並非以未滿 13 歲的兒童為對象，也不會故意收集兒童的資料。

## 聯絡與變更

隱私權相關問題：請在 {repo}/issues 開 issue。本政策的變更會公布在此頁面，並於頂端標示日期。
""",
    termos="""# Ætherna 使用條款

_最後更新：{data}_

使用 Ætherna 須遵守 **Apple 標準授權應用程式終端使用者授權合約**（{eula}），並另外適用以下條款。

## 內容

節目為**由人工智慧生成的對談**，並由**合成語音**朗讀。內容是對作品與主題的評論、分析與辯論，並非作品朗讀，且可能有錯誤。Ætherna 與所討論作品的作者、出版社、製作公司或權利人均無關聯。節目僅供個人使用，請勿散布。

## Ætherna Premium

- 按月自動續訂的訂閱，透過 App Store 購買。
- 確認購買時會向你的 Apple 帳號收費。
- 除非在目前期間結束前至少 24 小時取消，否則會自動續訂。續訂費用會在期間結束前 24 小時內收取。
- 你可以在 Apple 帳號設定中管理與取消訂閱。退款依 Apple 的規定辦理。

## 免費方案

免費方案一次可收聽一集，不能下載，也沒有同步文字。限制內容可能會變更，並會在 App 或本頁面公告。

## 帳號

帳號使用「透過 Apple 登入」。你可以隨時在「設定 → 帳號」中刪除帳號。

## 聯絡方式

請在 {repo}/issues 開 issue。
""",
    changelog="""# 新功能

## 1.0
- 首個版本：音訊深度解析與辯論、依類別瀏覽的目錄、系列整合（動畫與漫畫、各季）、無劇透順序、四種視覺風格與五種語言。
- Ætherna Premium：下載節目、同步文字，並可同時收聽多集。
""",
)

T["zh-Hans"] = dict(
    subtitulo="作品深度解析与辩论音频",
    promo="把书籍、电影、剧集、动画和历史变成音频对谈：导览式深度解析与辩论，随时随地收听。",
    palavras="播客,有声,音频,书籍,电影,剧集,动画,漫画,历史,辩论,解析,摘要,AI,收听",
    descricao="""Ætherna 把书籍、电影、剧集、动画和历史上的重大主题，变成可以随时随地收听的音频对谈。

每部作品都有两种形式：
• 深度解析：逐段导览剧情、角色与背景。
• 辩论：两个声音讨论作品的思想、亮点与争议。

内容特色
• 数百部作品、上千集节目，按类别整理：电影、剧集、历史、悬疑、犯罪、动画与漫画、游戏等。
• 系列整合：动画与漫画、各季与各部分，集中在同一个页面。
• 无剧透顺序：按照作品的顺序播放，如果某一集超前于你当前的进度会提醒你。
• 完整播放器：播放速度、后退 15 秒与快进 30 秒、睡眠定时器以及锁定屏幕控制。
• 四种视觉风格：电影资料馆、版本、信号与玻璃。
• 界面支持葡萄牙语、英语、德语和中文（繁体及简体）。

ÆTHERNA PREMIUM
免费方案一次可收听一集。升级 Premium 后你可以：
• 下载节目，离线收听；
• 一边播放一边阅读对谈文字；
• 想听几集就听几集，无需等待。

透明说明
对谈内容由人工智能生成，并由合成语音朗读，每一集都会标注。节目是对作品的评论与分析，并非作品朗读。Ætherna 与任何作者、出版社或制作公司均无关联。

订阅说明
Ætherna Premium 为按月自动续订的订阅。确认购买时将从你的 Apple 账户扣款。除非在当前周期结束前至少 24 小时取消，否则订阅将自动续订。你可以在 Apple 账户设置中管理或取消订阅。""",
    termos_rotulo="使用条款", priv_rotulo="隐私政策", suporte_rotulo="支持",
    novidades_rotulo="新功能",
    readme_intro="由 AI 生成、关于书籍、电影、剧集、动画与历史的音频对谈。本仓库不包含 App 代码，仅用于更新公告、支持与法律文件。",
    suporte="发现问题或有建议？请提交 issue：{repo}/issues/new/choose。issue 是公开的，请勿填写个人信息。",
    priv="""# Ætherna 隐私政策

_最后更新：{data}_

Ætherna 是一款收听作品相关音频对谈的 App。本政策说明 App 与 Ætherna 服务器会保存哪些数据，以及原因。

## 我们收集的数据

- **Apple 账户标识符。** 使用 Apple 登录时，我们会收到 Apple 为此 App 创建的匿名标识符。我们只保存其加密哈希值（HMAC），用来识别你的账户。**我们不会要求或保存你的姓名或电子邮件。**
- **设备会话。** 会话代码保存在设备的钥匙串中；服务器只保存其哈希值（SHA-256）。
- **订阅。** 如果你订阅 Premium，我们会保存产品、购买环境、到期日，以及 Apple 交易编号的加密哈希值，用于开通付费功能。**我们不会收到任何银行卡或支付信息**，扣款由 Apple 处理。
- **正在收听的节目。** 在免费方案中，服务器会记住你当前正在收听的那一集，以执行“一次一集”的规则。

## 我们不收集的数据

App 没有广告，不使用任何分析或追踪 SDK，也不会为了广告而出售或与第三方共享数据。你的收听记录、播放位置和偏好设置都保留**在设备上**。

## 设备上的数据

会话令牌只保存在此设备的钥匙串中。下载的节目保存在 App 的存储空间，不纳入备份。播放位置和偏好设置保存在 App 的存储空间。删除 App 会同时删除设备上的这些数据。

## 网络与服务提供商

App 通过 HTTPS、经由 Cloudflare 与 Ætherna 服务器连接；Cloudflare 会处理连接的 IP 地址以传输流量并保护服务。服务器只会在内存中短暂使用 IP 地址几分钟，用于限制注册滥用。

## 删除账户

在“设置 → 账户 → **删除我的账户**”中，App 会从服务器删除你的账户、会话、已记录的订阅以及正在收听的节目。如需停止订阅扣费，请同时在 Apple 账户设置中取消订阅。

## 儿童

Ætherna 并非面向 13 岁以下的儿童，也不会故意收集儿童的数据。

## 联系与变更

隐私相关问题：请在 {repo}/issues 提交 issue。本政策的变更会公布在此页面，并在顶部标注日期。
""",
    termos="""# Ætherna 使用条款

_最后更新：{data}_

使用 Ætherna 须遵守 **Apple 标准许可应用程序最终用户许可协议**（{eula}），并另外适用以下条款。

## 内容

节目为**由人工智能生成的对谈**，并由**合成语音**朗读。内容是对作品与主题的评论、分析与辩论，并非作品朗读，可能存在错误。Ætherna 与所讨论作品的作者、出版社、制作公司或权利人均无关联。节目仅供个人使用，请勿传播。

## Ætherna Premium

- 按月自动续订的订阅，通过 App Store 购买。
- 确认购买时将从你的 Apple 账户扣款。
- 除非在当前周期结束前至少 24 小时取消，否则将自动续订。续订费用会在周期结束前 24 小时内扣除。
- 你可以在 Apple 账户设置中管理和取消订阅。退款按 Apple 的规定处理。

## 免费方案

免费方案一次可收听一集，不能下载，也没有同步文字。限制内容可能会调整，并会在 App 或本页面公告。

## 账户

账户使用“通过 Apple 登录”。你可以随时在“设置 → 账户”中删除账户。

## 联系方式

请在 {repo}/issues 提交 issue。
""",
    changelog="""# 新功能

## 1.0
- 首个版本：音频深度解析与辩论、按类别浏览的目录、系列整合（动画与漫画、各季）、无剧透顺序、四种视觉风格与五种语言。
- Ætherna Premium：下载节目、同步文字，并可同时收听多集。
""",
)

# Chinês fica de fora da loja e do README até haver áudio; para liberar, ponha aqui.
LOJA_ATIVA = ["pt-BR", "en", "de"]
LOJA_LOCALE = {"pt-BR": "pt-BR", "en": "en-US", "de": "de-DE", "zh-Hant": "zh-Hant", "zh-Hans": "zh-Hans"}


def url(pagina, lingua):
    return f"{SITE}/{pagina}/{lingua}/"


def pagina(caminho, titulo, lingua, corpo):
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(f"---\ntitle: \"{titulo}\"\nlang: {lingua}\npermalink: /{caminho.parent.name}/{caminho.stem}/\n---\n\n{corpo}", encoding="utf-8")


def main():
    for lingua, t in T.items():
        f = dict(data=DATA[lingua], repo=REPO, eula=EULA)
        pagina(RAIZ / "privacy" / f"{lingua}.md", t["priv_rotulo"], lingua, t["priv"].format(**f))
        pagina(RAIZ / "terms" / f"{lingua}.md", t["termos_rotulo"], lingua, t["termos"].format(**f))
        pagina(RAIZ / "changelog" / f"{lingua}.md", t["novidades_rotulo"], lingua, t["changelog"])

    partes = ["# Ætherna\n",
              "<p align=\"center\"><img src=\"assets/icon.png\" width=\"160\" alt=\"Ætherna\"></p>\n"]
    for lingua, t in T.items():
        if lingua not in LOJA_ATIVA:
            continue
        partes.append(f"## {NOMES[lingua]}\n\n{t['readme_intro']}\n\n{t['descricao']}\n\n"
                      f"- [{t['priv_rotulo']}]({url('privacy', lingua)})\n"
                      f"- [{t['termos_rotulo']}]({url('terms', lingua)})\n"
                      f"- [{t['novidades_rotulo']}]({url('changelog', lingua)})\n"
                      f"- {t['suporte_rotulo']}: {t['suporte'].format(repo=REPO)}\n")
    readme = "\n".join(partes)
    (RAIZ / "README.md").write_text(readme, encoding="utf-8")
    (RAIZ / "index.md").write_text("---\ntitle: Ætherna\npermalink: /\n---\n\n" + readme.split("\n", 1)[1], encoding="utf-8")

    loja = {}
    for lingua, t in T.items():
        if lingua not in LOJA_ATIVA:
            continue
        d = t["descricao"] + f"\n\n{t['termos_rotulo']}: {url('terms', lingua)}\n{t['priv_rotulo']}: {url('privacy', lingua)}"
        assert len(d) <= 4000 and len(t["subtitulo"]) <= 30 and len(t["promo"]) <= 170 and len(t["palavras"]) <= 100, lingua
        loja[LOJA_LOCALE[lingua]] = dict(subtitle=t["subtitulo"], promotionalText=t["promo"], keywords=t["palavras"],
                                         description=d, privacyPolicyUrl=url("privacy", lingua),
                                         supportUrl=REPO + "/issues", marketingUrl=SITE + "/",
                                         termsUrl=url("terms", lingua))
    (RAIZ / "tools" / "loja.json").write_text(json.dumps(loja, ensure_ascii=False, indent=2), encoding="utf-8")
    print("ok", {k: (len(v["description"]), len(v["subtitle"]), len(v["keywords"])) for k, v in loja.items()})


if __name__ == "__main__":
    main()
