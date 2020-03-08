var app = angular.module('gameApp', []);

app.controller('gameCtrl', gameSetting);

app.config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('{a');
    $interpolateProvider.endSymbol('a}');
}]);

class card {
    constructor(name, avail, id, description) {
        this.id = id;
        this.name = name;
        this.avail = avail;
        this.description = description;
    }
}

class userState {
    constructor() {
        this.readyDrawCard = true;
    }
}

function getRandInt(min, max) {
    len = max - min;
    return min + Math.floor(len * Math.random());
}

function gameSetting($scope, $document) {
    $scope.user = null;
    $scope.centerCards = [
        {name: "king", avail: true, description: "is king", id: 0},
        {name: "queen", avail: true, description: "is queen", id: 1},
        {name: "jocker", avail: true, description: "is jocker", id: 2},
        {name: "cultist", avail: true, description: "is jocker", id: 3},
        {name: "cultist", avail: true, description: "is jocker", id: 4},
    ];
    $scope.centerCardsNum = 3;
    $scope.curCenterCards = [];

    $scope.shuffleCards = function(cards, num) {
        new_cards = [];
        drawed = [];

        i = 0;
        id = getRandInt(0, cards.length);
        while (i < num) {
            while (id in drawed) {
                id = getRandInt(0, cards.length)
            }

            new_cards.push(cards[id]);
            drawed.push(id);

            i += 1;
        }

        return new_cards;
    }

    $scope.drawCard = function(card) {
        if ($scope.user != null && $scope.user.readyDrawCard) {
            card.avail = false;
            $scope.user.readyDrawCard = false;
        }
    };

    $scope.getName = function (card) {
        if (card.avail) return card.name;
        else return "";
    }

    $scope.getDescription = function (card) {
        if (card.avail) return card.description;
        else return "";
    }

    $document.ready(function() {
        $scope.user = new userState();
    });
};
