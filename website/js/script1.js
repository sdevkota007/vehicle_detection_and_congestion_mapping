
      // This example requires the Places library. Include the libraries=places
      // parameter when you first load the API. For example:
      // <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
      // 27.717242,85.324050
      function initialize() {
        if(navigator.geolocation) {
          success = function(position) {
            createMap(position.coords.latitude, position.coords.longitude);
          };
          error = function() { initMap(); }

          navigator.geolocation.getCurrentPosition(success, error);
        }
        else {
          initMap();
        }
      }

      function initMap() {
        var map = new google.maps.Map(document.getElementById('googleMap'), {
          center: {lat: 27.717242, lng: 85.324050},
          zoom: 13
        });

        var bounds = new google.maps.LatLngBounds();
        

        // var input = /** @type {!HTMLInputElement} */(
        //     document.getElementById('pac-input1'));

        // var autocomplete = new google.maps.places.Autocomplete(input);
        // autocomplete.bindTo('bounds', map);

        // var infowindow = new google.maps.InfoWindow();
        
        var marker = new google.maps.Marker({
          map: map,
          anchorPoint: new google.maps.Point(0, -29)
        });

        function initAutocomplete() {
          autocomplete = new google.maps.places.Autocomplete(
              (document.getElementById('pac-input1')),
              {types: ['geocode']});
          autocomplete.addListener('place_changed', function() {
            fillInAddress(autocomplete, "");
          });

           autocomplete2 = new google.maps.places.Autocomplete(
              (document.getElementById('pac-input2')), {
                types: ['geocode']
              });
            autocomplete2.addListener('place_changed', function() {
              fillInAddress(autocomplete2, "2");
            });
        }

        google.maps.event.addDomListener(window, "load", initAutocomplete);

        google.maps.event.addListener(autocomplete,'place_changed', fillInAddress);

        function fillInAddress(autocomplete, unique) {
          var place = autocomplete.getPlace();
          if (!place.geometry) {
            window.alert("Autocomplete's returned place contains no geometry");
            return;
          }

          if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
          } else {
            map.setCenter(place.geometry.location);
            map.setZoom(17);  // Why 17? Because it looks good.
          }

          marker.setIcon(/** @type {google.maps.Icon} */({
            url: place.icon,
            size: new google.maps.Size(71, 71),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(17, 34),
            scaledSize: new google.maps.Size(35, 35)
          }));

          marker.setPosition(place.geometry.location);
          marker.setVisible(true);

          var address = '';
          if (place.address_components) {
            address = [
              (place.address_components[0] && place.address_components[0].short_name || ''),
              (place.address_components[1] && place.address_components[1].short_name || ''),
              (place.address_components[2] && place.address_components[2].short_name || '')
            ].join(' ');
          }
        }
      }



