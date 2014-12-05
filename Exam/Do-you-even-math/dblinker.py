from players import Players


class Dblinker():

    def get_scores(self, nickname):
        players = self.__session.query(Players).all()
        for player in players:
            if player.nickname == nickname:
                return player.highscore

    def update_table(self, nickname, current_scores):
        player_exists = self.session.query(Players).filter(Players.nickname == nickname).first()
        if player_exists.nickname:
            if self.get_scores(nickname) < current_scores:
                self.__session.query(Players).filter()
                Players.nickname == nickname.update({"highscore": current_scores})
                self.__session.commit()
            else:
                player = Players(nickname=nickname, highscore=current_scores)
                self.__session.add(player)
                self.__session.commit()

    def list_highscores(self, session):
        print("This is the current top10:")
        top_players = session.query(Players).order_by(Players.highscore.desc()).limit(10)
        for player in top_players:
            print (player)
