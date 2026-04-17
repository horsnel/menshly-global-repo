/* === Weather Widget — Open-Meteo (no API key, no IP ban) === */
(function() {
  var cities = [
    { name: 'Lagos', lat: 6.52, lon: 3.38 },
    { name: 'London', lat: 51.51, lon: -0.13 },
    { name: 'New York', lat: 40.71, lon: -74.01 },
    { name: 'Tokyo', lat: 35.68, lon: 139.69 },
    { name: 'Dubai', lat: 25.20, lon: 55.27 },
    { name: 'Beijing', lat: 39.90, lon: 116.40 }
  ];

  var weatherCodes = {
    0: 'Clear', 1: 'Mainly Clear', 2: 'Partly Cloudy', 3: 'Overcast',
    45: 'Foggy', 48: 'Rime Fog', 51: 'Light Drizzle', 53: 'Drizzle',
    55: 'Heavy Drizzle', 61: 'Light Rain', 63: 'Rain', 65: 'Heavy Rain',
    71: 'Light Snow', 73: 'Snow', 75: 'Heavy Snow', 80: 'Showers',
    81: 'Moderate Showers', 82: 'Violent Showers', 95: 'Thunderstorm',
    96: 'Thunderstorm + Hail', 99: 'Severe Thunderstorm'
  };

  var weatherIcons = {
    0: '\u2600\uFE0F', 1: '\uD83C\uDF24\uFE0F', 2: '\u26C5', 3: '\u2601\uFE0F',
    45: '\uD83C\uDF2B\uFE0F', 48: '\uD83C\uDF2B\uFE0F', 51: '\uD83C\uDF26\uFE0F',
    53: '\uD83C\uDF26\uFE0F', 55: '\uD83C\uDF27\uFE0F', 61: '\uD83C\uDF27\uFE0F',
    63: '\uD83C\uDF27\uFE0F', 65: '\uD83C\uDF27\uFE0F', 71: '\uD83C\uDF28\uFE0F',
    73: '\uD83C\uDF28\uFE0F', 75: '\u2744\uFE0F', 80: '\uD83C\uDF26\uFE0F',
    81: '\uD83C\uDF27\uFE0F', 82: '\uD83C\uDF27\uFE0F', 95: '\u26C8\uFE0F',
    96: '\u26C8\uFE0F', 99: '\u26C8\uFE0F'
  };

  function fetchWeather() {
    var latLon = cities.map(function(c) { return c.lat + ',' + c.lon; }).join('|');
    var url = 'https://api.open-meteo.com/v1/forecast?latitude=' +
      cities.map(function(c) { return c.lat; }).join(',') +
      '&longitude=' +
      cities.map(function(c) { return c.lon; }).join(',') +
      '&current=temperature_2m,weather_code&timezone=auto';

    fetch(url)
      .then(function(r) { return r.json(); })
      .then(function(data) {
        var container = document.getElementById('weatherContent');
        var loading = container ? container.parentElement.querySelector('.weather-loading') : null;
        if (!container || !data.current) return;
        if (loading) loading.style.display = 'none';
        container.style.display = 'block';

        var cityEls = document.querySelectorAll('.weather-city');
        cityEls.forEach(function(el, i) {
          if (!data.current.temperature_2m || !data.current.temperature_2m[i]) return;
          var temp = data.current.temperature_2m[i];
          var code = data.current.weather_code ? data.current.weather_code[i] : 0;
          el.querySelector('.weather-temp').textContent = Math.round(temp) + '\u00B0C';
          el.querySelector('.weather-desc').textContent = weatherCodes[code] || 'Clear';
          el.querySelector('.weather-icon').textContent = weatherIcons[code] || '\u2600\uFE0F';
        });

        var updated = document.getElementById('weatherUpdated');
        if (updated) {
          var now = new Date();
          updated.textContent = 'Updated ' + now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        }
      })
      .catch(function() {
        var loading = document.querySelector('.weather-loading');
        if (loading) loading.textContent = 'Weather unavailable';
      });
  }

  if (document.getElementById('weatherWidget')) {
    fetchWeather();
    setInterval(fetchWeather, 600000);
  }
})();
