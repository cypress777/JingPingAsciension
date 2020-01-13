var userAccessApp = angular.module('userAccessApp', []);

userAccessApp.controller('userAccessController', function($scope) {
    $scope.username = null;
    $scope.password = null;
    $scope.pattern = /^\s*\w*\s*$/;
});