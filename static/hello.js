var helloApp = angular.module('helloApp', ['ngAnimate']);

helloApp.controller('helloController', function($scope) {
    $scope.hideIntro = true;
    $scope.hideRules = true;
    $scope.hideTips = true;
});
