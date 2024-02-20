import pandas as pd
from user_info import User_Info
from constraint import Constraint

class Search_Engine():
    follower_constraint = None
    views_constraint = None
    saved_constraint = None
    likes_constraint = None
    comments_constraint = None
    shares_constraint = None
    downloaded_constraint = None
    whatsapp_constraint = None

    def __init__(self, file_name: str):
        self.user_info = User_Info(file_name)
    
    def query(self, username: str):
        pass

    def sort_by_followers(descending: bool):
        pass

    def sort_by_comment_count(descending: bool):
        pass

    def sort_by_download_count(descending: bool):
        pass

    def sort_by_whatsapp_lower(descending: bool):
        pass
    
    def set_followers_range(self, lower_bound: int, upper_bound: int):
        self.follower_constraint = Constraint(lower_bound, upper_bound)

    def set_saved_range(self, lower_bound: int, upper_bound: int):
        self.saved_constraint = Constraint(lower_bound, upper_bound)

    def set_comments_range(self, lower_bound: int, upper_bound: int):
        self.comments_constraint = Constraint(lower_bound, upper_bound)

    def set_likes_range(self, lower_bound: int, upper_bound: int):
        self.likes_constraint = Constraint(lower_bound, upper_bound)

    def set_downloaded_range(self, lower_bound: int, upper_bound: int):
        self.downloaded_constraint = Constraint(lower_bound, upper_bound)

    def set_shares_range(self, lower_bound: int, upper_bound: int):
        self.shares_constraint = Constraint(lower_bound, upper_bound)

    def set_shares_whatsapp_range(self, lower_bound: int, upper_bound: int):
        self.whatsapp_constraint = Constraint(lower_bound, upper_bound)
        