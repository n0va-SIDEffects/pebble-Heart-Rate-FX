/*
 * The settings page shown by the Pebble phone app.
 *
 * The page follows the phone's language, English unless the phone says German. The watch's own
 * language is a setting of its own, further down, because the two need not agree: someone may
 * read German on the phone and want English on the wrist, or the other way round.
 */
var DONATION_URL = 'https://buymeacoffee.com/SIDEffects';

var german = (typeof navigator !== 'undefined' && navigator.language &&
              navigator.language.toLowerCase().indexOf('de') === 0);

function t(en, de) {
  return german ? de : en;
}

var config = [
  {
    type: 'heading',
    defaultValue: 'Heart Rate FX'
  },
  {
    type: 'text',
    defaultValue: t('Your heartbeat as a trace, a sound and a light. The watch buttons also switch ' +
                    'vibration (select), sound (up) and the backlight (down) directly.',
                    'Herzschlag als Kurve, Ton und Licht. Die Tasten der Uhr schalten Vibration ' +
                    '(Auswahl), Ton (oben) und Beleuchtung (unten) auch direkt um.')
  },
  {
    type: 'section',
    items: [
      { type: 'heading', defaultValue: t('Sound', 'Ton') },
      {
        type: 'toggle',
        messageKey: 'SOUND_ON',
        label: t('Beep on every beat', 'Piep bei jedem Schlag'),
        description: t('Watches with a speaker only. Nothing is heard while the watch is silenced.',
                       'Nur Uhren mit Lautsprecher. Ist die Uhr stummgeschaltet, bleibt es still.'),
        defaultValue: true
      },
      {
        type: 'slider',
        messageKey: 'VOLUME',
        label: t('Volume', 'Lautstärke'),
        description: t('Above about 70 the small speaker distorts audibly.',
                       'Über etwa 70 verzerrt der kleine Lautsprecher hörbar.'),
        defaultValue: 65,
        min: 0,
        max: 100,
        step: 5
      },
      {
        type: 'select',
        messageKey: 'PITCH',
        label: t('Pitch', 'Tonhöhe'),
        defaultValue: 81,
        options: [
          { label: t('Low (660 Hz)', 'Tief (660 Hz)'), value: 76 },
          { label: t('Monitor (880 Hz)', 'Monitor (880 Hz)'), value: 81 },
          { label: t('High (1046 Hz)', 'Hoch (1046 Hz)'), value: 84 }
        ]
      }
    ]
  },
  {
    type: 'section',
    items: [
      { type: 'heading', defaultValue: t('Vibration', 'Vibration') },
      {
        type: 'toggle',
        messageKey: 'VIBE_ON',
        label: t('Buzz on every beat', 'Klick bei jedem Schlag'),
        description: t('The motor is audible through the speaker as well. Switch it off for a ' +
                       'clean monitor tone.',
                       'Der Motor ist auch im Lautsprecher hörbar. Für einen reinen Monitor-Ton ' +
                       'hier ausschalten.'),
        defaultValue: true
      },
      {
        type: 'select',
        messageKey: 'VIBE_MS',
        label: t('Length', 'Länge'),
        defaultValue: 25,
        options: [
          { label: t('Short', 'Kurz'), value: 15 },
          { label: t('Normal', 'Normal'), value: 25 },
          { label: t('Strong', 'Kräftig'), value: 40 }
        ]
      }
    ]
  },
  {
    type: 'section',
    items: [
      { type: 'heading', defaultValue: t('Display', 'Anzeige') },
      {
        type: 'select',
        messageKey: 'BACKLIGHT',
        label: t('Backlight', 'Beleuchtung'),
        description: t('Dimmed pulse leaves the light on and lifts it with every beat. Always on ' +
                       'costs noticeable battery and is meant for a short look.',
                       'Gedimmt pulsierend lässt das Licht an und hebt es bei jedem Schlag kurz ' +
                       'an. Dauerhaft an zieht spürbar Akku und ist für kurzes Zuschauen gedacht.'),
        defaultValue: 3,
        options: [
          { label: t('Dimmed pulse', 'Gedimmt pulsierend'), value: 3 },
          { label: t('Short flash per beat', 'Bei jedem Schlag kurz'), value: 1 },
          { label: t('Always on', 'Dauerhaft an'), value: 2 },
          { label: t('Leave it to the watch', 'Wie sonst auch'), value: 0 }
        ]
      },
      {
        type: 'color',
        messageKey: 'LIGHT_COLOR',
        label: t('Backlight colour', 'Farbe der Beleuchtung'),
        description: t('Watches with a colour backlight only, which means the Pebble Time 2. ' +
                       'Others light up white and cannot be dimmed, so there the backlight is ' +
                       'left to the watch.',
                       'Nur Uhren mit farbiger Beleuchtung, also die Pebble Time 2. Uhren ohne ' +
                       'sie leuchten weiß und können nicht gedimmt werden, dort bleibt die ' +
                       'Beleuchtung bei der Einstellung der Uhr.'),
        defaultValue: 0xff0000,
        allowGray: true
      },
      {
        type: 'slider',
        messageKey: 'LIGHT_FLOOR',
        label: t('Brightness between beats', 'Grundhelligkeit beim Pulsieren'),
        description: t('How brightly the backlight sits between two beats. At 0 it goes out.',
                       'Wie hell die Beleuchtung zwischen zwei Schlägen stehen bleibt. Bei 0 geht ' +
                       'sie ganz aus.'),
        defaultValue: 15,
        min: 0,
        max: 100,
        step: 5
      },
      {
        type: 'select',
        messageKey: 'SWEEP_MS',
        label: t('Trace speed', 'Kurvengeschwindigkeit'),
        defaultValue: 20,
        options: [
          { label: t('Slow', 'Langsam'), value: 40 },
          { label: t('Normal', 'Normal'), value: 20 },
          { label: t('Fast', 'Schnell'), value: 13 }
        ]
      },
      {
        type: 'select',
        messageKey: 'TRACE_COLOR',
        label: t('Trace colour', 'Kurvenfarbe'),
        description: t('Watches without a colour display always draw in white.',
                       'Uhren ohne Farbdisplay zeichnen immer weiß.'),
        defaultValue: 0,
        options: [
          { label: t('Green', 'Grün'), value: 0 },
          { label: t('Red', 'Rot'), value: 1 },
          { label: t('White', 'Weiß'), value: 2 },
          { label: t('Yellow', 'Gelb'), value: 3 },
          { label: t('Cyan', 'Türkis'), value: 4 }
        ]
      },
      {
        type: 'select',
        messageKey: 'LANGUAGE',
        label: t('Language on the watch', 'Sprache auf der Uhr'),
        defaultValue: 0,
        options: [
          { label: 'English', value: 0 },
          { label: 'Deutsch', value: 1 },
          { label: 'Français', value: 2 },
          { label: 'Español', value: 3 },
          { label: 'Italiano', value: 4 },
          { label: 'Nederlands', value: 5 },
          { label: 'Português', value: 6 },
          { label: 'Polski', value: 7 },
          { label: 'Svenska', value: 8 }
        ]
      }
    ]
  },
  {
    type: 'section',
    items: [
      { type: 'heading', defaultValue: t('Demo', 'Demo') },
      {
        type: 'toggle',
        messageKey: 'DEMO',
        label: t('Simulate a pulse', 'Puls simulieren'),
        description: t('Produces a pulse without the sensor, for showing the app. Holding the ' +
                       'lower button on the watch does the same.',
                       'Erzeugt einen Puls ohne Sensor, etwa zum Vorführen. Auf der Uhr schaltet ' +
                       'ein langer Druck auf die untere Taste dasselbe um.'),
        defaultValue: false
      }
    ]
  },
  {
    type: 'submit',
    defaultValue: t('Save', 'Speichern')
  }
];

if (DONATION_URL) {
  config.push({
    type: 'section',
    items: [
      { type: 'heading', defaultValue: t('Support', 'Unterstützen') },
      {
        type: 'text',
        defaultValue: t('The app is free and has no ads. If you enjoy it, a coffee is much ' +
                        'appreciated.',
                        'Die App ist kostenlos und ohne Werbung. Wenn sie dir Freude macht, ' +
                        'freue ich mich über einen Kaffee.')
      },
      { type: 'button', id: 'donate', primary: true, defaultValue: '☕ Buy me a coffee' }
    ]
  });
}

module.exports = config;
