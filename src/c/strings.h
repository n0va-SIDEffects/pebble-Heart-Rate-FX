/*
 * The few words the watch puts on screen, in English and German.
 *
 * English is the default: the app is published in an English-only store, and its screenshots have
 * to match what a buyer sees. German is a setting away.
 */
#pragma once

#include <stdint.h>

typedef enum {
  StrLanguageEnglish = 0,
  StrLanguageGerman = 1,
} StrLanguage;

typedef enum {
  StrBpm,
  StrSearching,
  StrLive,
  StrDemo,
  StrNoSensor,
  StrNoPermission,
  StrVibOn,
  StrVibOff,
  StrSoundOn,
  StrSoundOff,
  StrVibrationOn,
  StrVibrationOff,
  StrLightPulse,
  StrLightFlash,
  StrLightOn,
  StrLightNormal,
  StrCount,
} StringId;

void strings_set_language(uint8_t language);

const char *str(StringId id);
