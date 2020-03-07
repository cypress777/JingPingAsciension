var app = angular.module('gameApp', []);

app.controller('gameCtrl', game);

function game($scope) {
    console.log(document.readyState);
    $scope.cards = ["king", "queen", "joker"];
    $scope.used = [false, false, false];
    $scope.cardsNum = $scope.cards.length;
    $scope.test = "lalala";

    $scope.availCards = function() {
        cur = [];
        for (var i = 0; i <= $scope.cardsNum; i += 1) {
            if (!$scope.used[i]) {
                cur.push($scope.cards[i]);
            }
        }
        return cur;
    };
};
