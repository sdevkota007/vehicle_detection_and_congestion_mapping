
      // // This example requires the Places library. Include the libraries=places
      // // parameter when you first load the API. For example:
      // // <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
      // // 27.717242,85.324050
      // function initialize() {
        // if(navigator.geolocation) {
          // success = function(position) {
            // initMap(position.coords.latitude, position.coords.longitude);
          // };
          // error = function() { initMap(); }

          // navigator.geolocation.getCurrentPosition(success, error);
        // }
        // else {
          // initMap();
        // }
      // }

      // function initMap() {
        // var origin_place_id = null;
        // var destination_place_id = null;
        // var travel_mode = google.maps.TravelMode.DRIVING
        // var map = new google.maps.Map(document.getElementById('googleMap'), {
          // center: {lat: 27.717242, lng: 85.324050},
          // zoom: 13
        // });

        // var directionsService = new google.maps.DirectionsService;
        // var directionsDisplay = new google.maps.DirectionsRenderer({ polylineOptions: { strokeColor: "#123456" } });
        // directionsDisplay.setMap(map);
        // // directionsDisplay.setOptions({ suppressMarkers: true });

        // var origin_input = document.getElementById('pac-input1');
        // var destination_input = document.getElementById('pac-input2');
        
        // var origin_autocomplete = new google.maps.places.Autocomplete(origin_input);
        // origin_autocomplete.bindTo('bounds', map);
        // var destination_autocomplete =
            // new google.maps.places.Autocomplete(destination_input);
        // destination_autocomplete.bindTo('bounds', map);

        // function expandViewportToFitPlace(map, place) {
          // if (place.geometry.viewport) {
            // map.fitBounds(place.geometry.viewport);
          // } else {
            // map.setCenter(place.geometry.location);
            // map.setZoom(17);
          // }
        // }

        // origin_autocomplete.addListener('place_changed', function() {
          // var place = origin_autocomplete.getPlace();
          // if (!place.geometry) {
            // window.alert("Autocomplete's returned place contains no geometry");
            // return;
          // }
          // expandViewportToFitPlace(map, place);

          // // If the place has a geometry, store its place ID and route if we have
          // // the other place ID
          // origin_place_id = place.place_id;
          // route(origin_place_id, destination_place_id, travel_mode,
                // directionsService, directionsDisplay);
        // });

        // destination_autocomplete.addListener('place_changed', function() {
          // var place = destination_autocomplete.getPlace();
          // if (!place.geometry) {
            // window.alert("Autocomplete's returned place contains no geometry");
            // return;
          // }
          // expandViewportToFitPlace(map, place);

          // // If the place has a geometry, store its place ID and route if we have
          // // the other place ID
          // destination_place_id = place.place_id;
          // route(origin_place_id, destination_place_id, travel_mode,
                // directionsService, directionsDisplay);
        // });

        // function route(origin_place_id, destination_place_id, travel_mode,
                       // directionsService, directionsDisplay) {
          // if (!origin_place_id || !destination_place_id) {
            // return;
          // }
          // directionsService.route({
            // origin: {'placeId': origin_place_id},
            // destination: {'placeId': destination_place_id},
            // provideRouteAlternatives: true,
            // travelMode: travel_mode
          // }, function(response, status) {
            // if (status === google.maps.DirectionsStatus.OK) {
              // for (var i = 0, len = response.routes.length; i < len; i++) {
              // // directionsDisplay.setDirections(response);
                // new google.maps.DirectionsRenderer({
                    // map: map,
                    // directions: response,
                    // routeIndex: i,
                    // polylineOptions: { strokeColor: "GREEN" },
                    // suppressMarkers: false
                // });
                

              // }

              // var polyline1 = new google.maps.Polyline({
                  // path: [],
                  // strokeColor: "#DD71D8",
                  // strokeWeight: 4
              // });
              // var polyline2 = new google.maps.Polyline({
                  // path: [],
                  // strokeColor: "#0000ff",
                  // strokeWeight: 4
              // });

              // var bounds = new google.maps.LatLngBounds();

              // var path1 = response.routes[0].overview_path;
              // var legs1 = response.routes[0].legs;
              // for (i = 0; i < legs1.length; i++) {
                  // var steps1 = legs1[i].steps;
                  // for (j = 0; j < steps1.length; j++) {
                      // var nextSegment1 = steps1[j].path;
                      // for (k = 0; k < nextSegment1.length; k++) {
                          // polyline1.getPath().push(nextSegment1[k]);
                          // bounds.extend(nextSegment1[k]);
                      // }
                  // }
              // }
              // console.log('polyline1 length:' +polyline1.getPath().getLength());

              // if (polyline2.getPath().getLength() > 1) {
                  // getPolylineIntersection();
              // }
              // directionsDisplay.setDirections(response);
              // // new google.maps.renderer.setDirections(response);

              // var path2 = response.routes[1].overview_path;
              // var legs2 = response.routes[1].legs;
              // for (i = 0; i < legs2.length; i++) {
                  // var steps2 = legs2[i].steps;
                  // for (j = 0; j < steps2.length; j++) {
                      // var nextSegment2 = steps2[j].path;
                      // for (k = 0; k < nextSegment2.length; k++) {
                          // polyline2.getPath().push(nextSegment2[k]);
                          // bounds.extend(nextSegment2[k]);
                      // }
                  // }
              // }
              // console.log('polyline2 length:' +polyline2.getPath().getLength());
			  // polyline2.setMap(map);
              // if (polyline1.getPath().getLength() > 1) {
                  // getPolylineIntersection();
              // }
              // directionsDisplay.setDirections(response);
              // // renderer.setDirections(response);

              // function getPolylineIntersection() {
                // for (var i = 0; i < polyline1.getPath().getLength(); ) {
                    
                    // //find match beginning
                    // var match = -1; 
                    // for (var j = 0; j < polyline2.getPath().getLength(); j++) {
                        // if (polyline1.getPath().getAt(i).equals(polyline2.getPath().getAt(j))) {
                            // match = j;
                            // console.log('match found' +match);
                            // break;
                        // }
                    // }
                    
                    // var matching_points = [];
                    
                    // if(match > -1) {
                      
                        // while(polyline1.getPath().getAt(i).equals(polyline2.getPath().getAt(match)) 
                                // && i < polyline1.getPath().getLength() && match < polyline2.getPath().getLength())
                                 // {
                            // matching_points.push(polyline1.getPath().getAt(i));
                            // i++;
                            // match++;
                        // }
                        // console.log('match points: ' +matching_points.length);
                        // console.log('points' +matching_points);
                        
                        // if(matching_points.length > 0) {
                          // for(var i=0; i=matching_points.length; i++){
                            // console.log('YESSSSSSSSSSSSSS')
                            // var overlap = new google.maps.Polyline({
                                  // path: [],
                                  // strokeColor: "RED",
                                  // strokeWeight: 12
                              // });
                          // }
						// overlap.setMap(map);
                        // }
                        
                    // }

                     // else {
                        // i++;
                    // }
                    // console.log('points' +matching_points);
                // }
            // }

                // // var pointsArray1 = [];
                // // pointsArray1 = response.routes[0].overview_path;
                // // alert(pointsArray1);
                // // alert(pointsArray1.length);

                // // var pointsArray2 = [];
                // // pointsArray2 = response.routes[1].overview_path;
                // // alert(pointsArray2);
                // // alert(pointsArray2.length);

                // // if(pointsArray1[0].equals(pointsArray2[0])){
                // //   alert('its equal');
                // // } else {
                // //   alert('its not equal');
                // // }

          
                // // var hiddenElement = document.createElement('a');

                // // hiddenElement.href = 'data:attachment/text,' + encodeURI(pointsArray1);
                // // hiddenElement.target = '_blank';
                // // hiddenElement.download = 'File.csv';
                // // hiddenElement.click();

                

                // // for (var i = 0, len = pointsArray2.length; i < len; i++){
                // //   if(pointsArray1[i].equals(pointsArray2[i]))
                // //   {
                    
                    
                // //   } else {
                // //     var point1 = new google.maps.Marker ({
                // //         position:pointsArray1[i-1],
                // //         draggable:true,
                // //         map:map,
                // //         flat:true
                // //     });
                // //     break;
                // //   }
                // // }

            // } else {
              // window.alert('Directions request failed due to ' + status);
            // }
          // });
        // }
      // }

      // // function LoadRoute(){
      // //   var request = {
      // //     oriign: new google.maps.Latlng(matching_points[0]),
      // //     destination: new googel.maps.Latlng(matching_points[matching_points.length-1]),
      // //     waypoints: [{
      // //       for(var i=1, i=matching_points.length-2, i++){
      // //         location : new google.maps.Latlng(matching_points[i])
      // //       }
      // //     }],
      // //   };

      // // }
	  
	var hiddenElement = document.createElement('a');

	hiddenElement.href = 'data:attachment/text,' + encodeURI(pointsArray1);
	hiddenElement.target = '_blank';
	hiddenElement.download = 'File.csv';
	hiddenElement.click();


