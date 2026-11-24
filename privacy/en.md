---
title: "Privacy Policy"
lang: en
permalink: /privacy/en/
---

# Ætherna Privacy Policy

_Last updated: November 24, 2026_

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

Privacy questions: open an issue at https://github.com/JoaoZaokk/aetherna-app/issues. Changes to this policy appear on this page, with the date at the top.
