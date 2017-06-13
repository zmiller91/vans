define([
], function(){return{init: function(app) {

        app.controller("ListingsCtrl", function(ListingsData, $scope, $window)
        {
            $scope.listings = [];
            $scope.loading = false;
            
            $scope.viewListing = function(url) {
                $window.open(url, '_blank');
            }

            var update = function() {
                $scope.loading = true;
                ListingsData.get(
                    function(listings) {
                        $scope.listings = listings;
                        $scope.loading = false;
                    },
                    function() {
                        $scope.loading = false;
                    }
                );
            };
            
            angular.element(document).ready(update);
        })

        .directive("listings", function() {
          return {
            templateUrl: 'html/listings.html'
          };
        })

        .service('ListingsData', ['$http', function($http) 
        {
            this.listings = [];
            this.houseTypes = [];
            
            // Generic GET request
            this.get = function(success, error)
            {
                var $this = this;
                $http.get('api/listings').then(
                    function(response)  {
                        $this.listings = response.data;
                        if(success){success($this.listings);};
                    },  
                    error
                );
            };
        }]);
}};});