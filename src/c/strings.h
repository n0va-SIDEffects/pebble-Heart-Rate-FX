/*
 * The few words the watch puts on screen.
 *
 * English is the default: the app is published in an English-only store, and its screenshots have
 * to match what a buyer sees. Any other language is one setting away.
 *
 * Only languages written in Latin script are offered. The watch's own font was checked on the
 * hardware and draws the whole of Latin Extended-A, so accented and Polish letters come out
 * properly; Cyrillic and Greek would need a font of their own.
 */
#pragma once

#include <stdint.h>

typedef enum {
  StrLanguageEnglish = 0,
  StrLanguageGerman,
  StrLanguageFrench,
  StrLanguageSpanish,
  StrLanguageItalian,
  StrLanguageDutch,
  StrLanguagePortuguese,
  StrLanguagePolish,
  StrLanguageSwedish,
  StrLanguageCount,
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
