import pandas as pd
import json

"""
Goal: Implement social media insights engine
1) Given a username, retrieve/order by follower count, video views, saved, comments, likes, downloaded, and/or shares
2) Order by follower count, video views, saved, comments, likes, downloaded, and/or shares, retrieve users
"""

class User_Info():
    user_profiles = pd.DataFrame()
    original_posts = pd.DataFrame()
    social_medias = pd.DataFrame()
    posts_infos = pd.DataFrame()

    def __init__(self, file_name: str):
        self.__load_data__(file_name)

    def __load_data__(self, file_name: str):
        with open(file_name, 'r') as file:
            user_infos = json.load(file)

        for data in user_infos:
            user_profile = data["user_profile"]
            original_post = data['original_post']
            social_media = data['social_media']
            posts_info = data['posts_info']
            author_id = user_profile["author_uid"]
            
            original_post["author_id"] = author_id
            social_media["author_id"] = author_id
            
            for post_info in posts_info:
                post_info["author_id"] = author_id
                self.posts_infos = pd.concat([self.posts_infos, pd.DataFrame([post_info])], ignore_index=True)
            
            self.social_medias = pd.concat([self.social_medias, pd.DataFrame([social_media])], ignore_index=True)
            self.original_posts = pd.concat([self.original_posts, pd.DataFrame([original_post])], ignore_index=True)
            self.user_profiles = pd.concat([self.user_profiles, pd.DataFrame([user_profile])], ignore_index=True)