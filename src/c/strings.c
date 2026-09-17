#include "strings.h"

static const char *const s_english[StrCount] = {
  [StrBpm] = "BPM",
  [StrSearching] = "Searching...",
  [StrLive] = "Live",
  [StrDemo] = "Demo",
  [StrNoSensor] = "No pulse sensor (hold DOWN for demo)",
  [StrNoPermission] = "No health permission",
  [StrVibOn] = "Vib on",
  [StrVibOff] = "Vib off",
  [StrSoundOn] = "Sound on",
  [StrSoundOff] = "Sound off",
  [StrVibrationOn] = "Vibration on",
  [StrVibrationOff] = "Vibration off",
  [StrLightPulse] = "Light: pulse",
  [StrLightFlash] = "Light: flash",
  [StrLightOn] = "Light: on",
  [StrLightNormal] = "Light: normal",
};

static const char *const s_german[StrCount] = {
  [StrBpm] = "BPM",
  [StrSearching] = "Suche Puls...",
  [StrLive] = "Live",
  [StrDemo] = "Demo",
  [StrNoSensor] = "Kein Pulssensor (DOWN lang: Demo)",
  [StrNoPermission] = "Keine Health-Freigabe",
  [StrVibOn] = "Vib an",
  [StrVibOff] = "Vib aus",
  [StrSoundOn] = "Ton an",
  [StrSoundOff] = "Ton aus",
  [StrVibrationOn] = "Vibration an",
  [StrVibrationOff] = "Vibration aus",
  [StrLightPulse] = "Licht: Puls",
  [StrLightFlash] = "Licht: Blitz",
  [StrLightOn] = "Licht: an",
  [StrLightNormal] = "Licht: normal",
};

static const char *const *s_table = s_english;

void strings_set_language(uint8_t language) {
  s_table = (language == StrLanguageGerman) ? s_german : s_english;
}

const char *str(StringId id) {
  return (id < StrCount) ? s_table[id] : "";
}
