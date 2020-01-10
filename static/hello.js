var helloApp = angular.module('helloApp', ['ngAnimate']);

helloApp.controller('helloController', function($scope) {
    $scope.titles = ["Intro", "Rules", "Tips"];
    $scope.descriptions = ["Intro is ...", 
                           "Rules are ...",
                           "Tips are ..."]
    $scope.activeTitles = ["title-active-intro", "title-active-rules", "title-active-tips"];
    $scope.hideTitles = [true, true, true];
    $scope.titleNum = $scope.titles.length;

    $scope.range = function(min, max, step) {
        step = step || 1;
        var input = [];
        for (var i = min; i <= max; i += step) {
            input.push(i);
        }
        return input;
    };

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

