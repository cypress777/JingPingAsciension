var helloApp = angular.module('helloApp', ['ngAnimate']);

helloApp.controller('helloController', function($scope) {
    $scope.titles = ["Intro", "Rules", "Tips"];
    $scope.descriptions = ["Intro is ...", 
                           "Rules are ...",
                           "Tips are ..."]
    $scope.activeTitles = ["title-active-intro", "title-active-rules", "title-active-tips"];
    $scope.hideTitles = [true, true, true];

    $scope.getTitle = function(id) {
        return $scope.titles[id];
    }

    $scope.getDescription = function(id) {
        return $scope.descriptions[id];
    }

    $scope.getClass = function(id) {
        return $scope.hideTitles[id] ? "" : $scope.activeTitles[id];
    }

    $scope.flipHide = function(id) {
        $scope.hideTitles[id] = !$scope.hideTitles[id];
    }

    $scope.getHide = function(id) {
        return $scope.hideTitles[id];
    }
});

