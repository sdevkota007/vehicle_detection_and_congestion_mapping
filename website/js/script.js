
      // This example requires the Places library. Include the libraries=places
      // parameter when you first load the API. For example:
      // <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
      // 27.717242,85.324050
      function initialize() {
        if(navigator.geolocation) {
          success = function(position) {
            initMap(position.coords.latitude, position.coords.longitude);
          };
          error = function() { initMap(); }

          navigator.geolocation.getCurrentPosition(success, error);
        }
        else {
          initMap();
        }
      }

      function initMap() {
        var origin_place_id = null;
        var destination_place_id = null;
        var travel_mode = google.maps.TravelMode.DRIVING
        var map = new google.maps.Map(document.getElementById('googleMap'), {
          center: {lat: 27.717242, lng: 85.324050},
          zoom: 14
        });
		
		// alert(myvar[0]);

        var directionsService = new google.maps.DirectionsService;
        var directionsDisplay = new google.maps.DirectionsRenderer;
        directionsDisplay.setMap(map);

        var origin_input = document.getElementById('pac-input1');
        var destination_input = document.getElementById('pac-input2');
        
        var origin_autocomplete = new google.maps.places.Autocomplete(origin_input);
        origin_autocomplete.bindTo('bounds', map);
        var destination_autocomplete =
            new google.maps.places.Autocomplete(destination_input);
        destination_autocomplete.bindTo('bounds', map);

        function expandViewportToFitPlace(map, place) {
          if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
          } else {
            map.setCenter(place.geometry.location);
            map.setZoom(17);
          }
        }

        origin_autocomplete.addListener('place_changed', function() {
          var place = origin_autocomplete.getPlace();
          if (!place.geometry) {
            window.alert("Autocomplete's returned place contains no geometry");
            return;
          }
          expandViewportToFitPlace(map, place);

          // If the place has a geometry, store its place ID and route if we have
          // the other place ID
          origin_place_id = place.place_id;
          route(origin_place_id, destination_place_id, travel_mode,
                directionsService, directionsDisplay);
        });

        destination_autocomplete.addListener('place_changed', function() {
          var place = destination_autocomplete.getPlace();
          if (!place.geometry) {
            window.alert("Autocomplete's returned place contains no geometry");
            return;
          }
          expandViewportToFitPlace(map, place);

          // If the place has a geometry, store its place ID and route if we have
          // the other place ID
          destination_place_id = place.place_id;
          route(origin_place_id, destination_place_id, travel_mode,
                directionsService, directionsDisplay);
        });

        function route(origin_place_id, destination_place_id, travel_mode,
                       directionsService, directionsDisplay) {
          if (!origin_place_id || !destination_place_id) {
            return;
          }
          directionsService.route({
            origin: {'placeId': origin_place_id},
            destination: {'placeId': destination_place_id},
			provideRouteAlternatives: true,
            travelMode: travel_mode
          }, function(response, status) {
            if (status === google.maps.DirectionsStatus.OK) {
              // directionsDisplay.setDirections(response);
			  for (var i = 0, len = response.routes.length; i < len; i++) {
              // directionsDisplay.setDirections(response);
                new google.maps.DirectionsRenderer({
                    map: map,
                    directions: response,
                    routeIndex: i,
                    // polylineOptions: { strokeColor: "GREEN" },
                    suppressMarkers: false
                });
			  }
			
			
			
			
			var pointsArray2 = [];
			pointsArray2 = response.routes[1].overview_path;
			for(var i=0; i<pointsArray2.length; i++){
			  var overlap = new google.maps.Polyline({
				  path: pointsArray2,
				  strokeColor: myvar[1],
				  strokeWeight: 4
			  });
				overlap.setMap(map);
			}
			
			var pointsArray1 = [];
			pointsArray1 = response.routes[0].overview_path;
			console.log(pointsArray1);
			// alert(pointsArray1);
			for(var i=0; i<pointsArray1.length; i++){
			  var overlap = new google.maps.Polyline({
				  path: pointsArray1,
				  strokeColor: myvar[0],
				  strokeWeight: 4
			  });
				overlap.setMap(map);
			}
			
			
			  
            } else {
              window.alert('Directions request failed due to ' + status);
            }
          });
        }
      }


