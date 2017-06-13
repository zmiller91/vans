define([
    'listings',
],

  function(listings){
      
    // Create the base module for the page
    var vans = angular.module('vans', []);
    
    // Init the controllers, directives, and services for all the components
    // on the page
    listings.init(vans);
    
    // Bootstrap the page
    angular.bootstrap(document, ['vans']);
});