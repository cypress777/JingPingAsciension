var loginApp = angular.module('loginApp', []);

loginApp.controller('loginController', function($scope) {
    $scope.username = null;
    $scope.password = null;
});

var signupApp = angular.module('signupApp', []);

signupApp.controller('signupController', function($scope) {
    $scope.username = null;
    $scope.password = null;
});
