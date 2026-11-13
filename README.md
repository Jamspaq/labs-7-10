# Командалық жоба — Lab 7–10

Қатысушылар: **Альмансур — @Jamspaq**, **Нурперзент — @NurperzentTagaibek**.

## Беттер

- [Басты бет](index.html): екі қатысушыға ортақ навигация.
- [Альмансур](almansur.html): басты бет және HTML бағыты.
- [Нурперзент](nurperzent.html): стильдер және CI/CD бағыты.

## Іске қосу және тексеру

`index.html` файлын браузерде ашыңыз. Python 3.10 немесе жаңарақ нұсқамен:

```sh
python scripts/check_html.py
python scripts/build.py
python -m http.server 8000 --directory dist
```

Браузерде http://localhost:8000 ашыңыз.

HTML Check негізгі құрылымды, тегтердің жабылуын, метадеректерді және жергілікті сілтемелерді тексереді; толық W3C валидациясын алмастырмайды.

## Lab 7 — Version Control

Өзгерістер жеке `feature-update` тармағында сақталады, Pull Request арқылы `main` тармағына біріктіріледі. Review кезінде HTML құрылымын, файл атауларын және навигацияны тексеру керек.

## Lab 8 — Issues және Projects

Кемінде үш Issue: құжаттама, CI/CD тексеру, v1.0.0 релизі. Kanban күйлері: To Do → In Progress → Review → Done. PR сипаттамасындағы `Closes #1` Issue-ды merge кезінде жабады.

Әр қатысушы өз аккаунтынан кемінде бір Issue ашуы керек. Бір аккаунтпен жасалған әрекеттер екі адамның қатысуын растамайды.

## Lab 9 — CI/CD

- `html-check.yml`: push және PR кезінде HTML тексеру.
- `ci-cd.yml`: main/master push, PR және v* тегтері кезінде test + build.
- Build сайтты `dist/` каталогына жинап, `website` artifact жүктейді.
- Deploy build аяқталған соң push кезінде artifact-ты staging каталогына жүктейді және файлдарды тексереді.

Deploy — тапсырмада көрсетілген шартты орналастыру; қоғамдық хостингке сайт шығармайды.

## Lab 10 — Versioning

Алғашқы тұрақты нұсқа: `v1.0.0`. Өзгерістер [CHANGELOG.md](CHANGELOG.md) файлында. Тег push кезінде CI/CD іске қосылады. GitHub Releases ішінде сол тегке release жарияланады.

## Қатысушылардың жұмысы

Беттерде міндеттердің ұсынылған бөлінісі берілген. Нақты үлес GitHub-тағы авторлар, Issues және review әрекеттері бойынша анықталады.
