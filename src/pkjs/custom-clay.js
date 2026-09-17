/*
 * Runs inside the settings page. Clay turns this function into text and drops it into the page, so
 * it cannot require anything or reach anything outside itself: every value it needs must be
 * written out here. An earlier version read the address from config.js, which left a require call
 * in the page and stopped it from loading at all.
 *
 * Keep the address below in step with DONATION_URL in config.js.
 *
 * The button wears Buy Me a Coffee's own colours instead of Clay's orange, so it looks like the
 * button people know from the site: yellow #FFDD00 with black lettering. Clay's own rules are
 * plain class selectors, so the ones here carry !important to be sure they win wherever the page
 * is rendered. The mixed case and the pressed shade are part of that look as well, which is why
 * Clay's uppercase is switched off.
 */
module.exports = function() {
  var clayConfig = this;
  var url = 'https://buymeacoffee.com/SIDEffects';

  var BMC_CSS = [
    'button[data-donate="bmc"] {',
    '  background-color: #ffdd00 !important;',
    '  color: #000000 !important;',
    '  text-transform: none !important;',
    '  -webkit-tap-highlight-color: rgba(255, 221, 0, 0.4) !important;',
    '}',
    'button[data-donate="bmc"]:active {',
    '  background-color: #f2d100 !important;',
    '}'
  ].join('\n');

  clayConfig.on(clayConfig.EVENTS.AFTER_BUILD, function() {
    var button = clayConfig.getItemById('donate');
    if (!button) {
      return;
    }

    if (!document.getElementById('bmc-style')) {
      var style = document.createElement('style');
      style.id = 'bmc-style';
      style.appendChild(document.createTextNode(BMC_CSS));
      document.head.appendChild(style);
    }

    button.on('click', function() {
      var opened = null;
      try {
        opened = window.open(url, '_blank');
      } catch (e) {
        opened = null;
      }
      if (!opened) {
        window.location.href = url;
      }
    });
  });
};
