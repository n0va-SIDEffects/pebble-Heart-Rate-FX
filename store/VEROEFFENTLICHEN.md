# Heart Rate FX im Pebble Appstore einreichen

Alles Nötige liegt in `store/release/`. Am **PC im Desktop-Browser** einreichen: Vom Handy aus
antwortet das Portal auf den Upload mit einem nichtssagenden Fehler 400.

## Was wofür ist

| Datei | Verwendung |
| --- | --- |
| `Heart-Rate-FX-1.0.pbw` | die App selbst, wird als Release hochgeladen |
| `icon_80.png` | Store-Icon, ohne Alphakanal |
| `icon_144.png`, `icon_48.png` | falls das Portal zusätzlich danach fragt |
| `banner_720x320.png` | Kopfbild der Listung |
| `screenshots_emery/` | fünf Bilder für die Pebble Time 2, in dieser Reihenfolge |
| `screenshots_diorite/` | drei Bilder für die Pebble 2 |
| `description_en.txt` | erste Zeile Kurzbeschreibung, Rest Beschreibung (1572 von 1600 Zeichen) |
| `RELEASE_NOTES.md` | Text fürs Release |

## Schritte im Portal

Portal: https://developer.repebble.com/dashboard, Konto der Pebble-Handy-App.

1. **Add Watchapp**.
2. Grunddaten eintragen:
   - Title: `Heart Rate FX`
   - Category: `Health & Fitness`, ersatzweise `Tools & Utilities`
   - Support email: deine Adresse
   - Source code URL: `https://github.com/n0va-SIDEffects/pebble-Heart-Rate-FX`
     (**das Repo muss dafür öffentlich sein**, siehe Checkliste)
   - Icon: `icon_80.png`
3. **Create**.
4. **Add a release**: `Heart-Rate-FX-1.0.pbw` hochladen, Release Notes aus `RELEASE_NOTES.md`.
   Seite neu laden, dann neben dem Release **Publish**.
5. **Manage Asset Collections**, je eine pro Plattform:
   - `emery` (Pebble Time 2): Beschreibung aus `description_en.txt`, die fünf Bilder aus
     `screenshots_emery/` in der Reihenfolge 1 bis 5, Banner `banner_720x320.png`
   - `diorite` (Pebble 2): dieselbe Beschreibung, die drei Bilder aus `screenshots_diorite/`
   - `flint` und `gabbro` haben noch keine eigenen Bilder. Entweder auslassen oder die
     `emery`-Bilder verwenden, sie werden dann skaliert gezeigt.
6. Oben **Publish**, oder erst **Publish Privately**, um die Listung zu prüfen.

## Updates später

Schneller über die Kommandozeile, im Projektordner:

```sh
pebble login
pebble build
pebble publish --release-notes "Was neu ist"
```

`version` in `package.json` vorher erhöhen, immer im Format `Major.Minor`.
Die UUID `72901d59-fab9-449d-b3cd-43926085b2fc` darf sich nie ändern, sonst gilt das Update als
neue App.

## Checkliste

- [ ] Repo `pebble-Heart-Rate-FX` auf öffentlich gestellt, sonst führt der Quellcode-Link ins Leere
- [ ] `version` steht auf `1.0`, nicht `1.0.0`
- [ ] Icon ohne Alphakanal hochgeladen (`icon_80.png` ist bereits RGB)
- [ ] Beschreibung unter 1600 Zeichen (geprüft: 1572)
- [ ] Am PC eingereicht, nicht am Handy
- [ ] Die `.pbw` einmal auf der echten Uhr installiert und ausprobiert
