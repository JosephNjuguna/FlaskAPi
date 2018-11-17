class UserData():
    def Rides(self):
        rides = [
         {
            'id':1,
            'ride':"town",
            'duration': "45min",
            'accept':"ACCEPTED",
            'request':"REQUESTED",
            'create_date':"18-03-1998",
            'body': "the route we will be taking will be through nyayo not kenyatta as earlier said"
        },
        {
            'id':2,
            'ride':"Andela",
            'duration': "15min",
            'accept':"ACCEPTED",
            'request':"REQUESTED",
        }]
        return rides

    def users(self):
        users = [
             {
                'id':1,
                'name':"Joseph",
                'phonenumber':0701,
                'gender':"male",
                'location':"Rongai"
            },
            {
                'id':2,
                'name':"Ian",
                'phonenumber':0755,
                'gender':"male",
                'location':"Westlands"

            }]
        return users

#sudo apt-get install mysql-server libmysqlclient-dev
