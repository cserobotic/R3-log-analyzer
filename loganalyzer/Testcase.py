# -*- coding: utf-8 -*-

from loganalyzer.Parser import *
from loganalyzer.Game import *
from loganalyzer.Analyzer import *
import glob
import os
import pandas as pd

directory_path='/home/sana/robotic/R32D/src'
log_files=[]
for file in os.listdir(directory_path):
    if file.endswith('.rcg'):
        log_files.append(directory_path+'/'+file.removesuffix('.rcg'))

all_games=[]
for path in log_files: 
      df_right=dict()
      df_left=dict()
      parser = Parser(path)
      game = Game(parser)

      analyzer = Analyzer(game)
      analyzer.analyze()

      
      df_right["Right Team"] = analyzer.game.right_team.name
      df_right["Game result"] = analyzer.status_r
      df_right["Goals"] = str(analyzer.game.right_goal)
      df_right["True Pass"] = str(analyzer.pass_r)
      df_right["Wrong Pass"] = str(analyzer.intercept_l)   
      df_right["Pass in Length"] = str(analyzer.pass_in_length_r)
      df_right["Pass in Width"] = str(analyzer.pass_in_width_r)
      df_right["Pass Accuracy"] = str(analyzer.pass_accuracy_r)
      df_right["on_target_shoot"] = str(analyzer.on_target_shoot_r)
      df_right["off_target_shoot"] = str(analyzer.off_target_shoot_r)
      df_right["Shoot in Length"] = str(analyzer.shoot_in_length_r)
      df_right["Shoot in Width"] = str(analyzer.shoot_in_width_r)
      df_right["Shoot Accuracy"] = str(analyzer.shoot_accuracy_r)
      df_right["Possession"] = str(analyzer.possession_r)
      df_right["Stamina Usage"] = analyzer.used_stamina_agents_r
      df_right["moved Distance"] = analyzer.team_moved_distance_r
      df_right["Average Distance 10 Player"] = str(analyzer.average_distance_10p_r)
      df_right["Average Stamina 10 Player"] = str(analyzer.average_stamina_10p_r)
      df_right["Average Stamina Per distance 10 Player"] = str(analyzer.av_st_per_dist_10p_r)
      df_right["Stamina per Distance"] = str(analyzer.used_per_distance_r)
      df_left["Left Team"] = analyzer.game.left_team.name
      df_left["Game result"] = analyzer.status_l
      df_left["Goals"] = str(analyzer.game.left_goal)
      df_left["True Pass"] = str(analyzer.pass_l)
      df_left["Wrong Pass"] = str(analyzer.intercept_r)
      df_left["Pass in Length"] = str(analyzer.pass_in_length_l)
      df_left["Pass in Width"] = str(analyzer.pass_in_width_l)
      df_left["Pass Accuracy"] = str(analyzer.pass_accuracy_l)
      df_left["on_target_shoot"] = str(analyzer.on_target_shoot_l)
      df_left["off_target_shoot"] = str(analyzer.off_target_shoot_l)
      df_left["Shoot in Length"] = str(analyzer.shoot_in_length_l)
      df_left["Shoot in Width"] = str(analyzer.shoot_in_width_l)
      df_left["Shoot Accuracy"] = str(analyzer.shoot_accuracy_l)
      df_left["Possession"] = str(analyzer.possession_l)
      df_left["Stamina Usage"] = analyzer.used_stamina_agents_l
      df_left["moved Distance"] = analyzer.team_moved_distance_l
      df_left["Average Distance 10 Player"] = str(analyzer.average_distance_10p_l)
      df_left["Average Stamina 10 Player"] = str(analyzer.average_stamina_10p_l)
      df_left["Average Stamina Per distance 10 Player"] = str(analyzer.av_st_per_dist_10p_l)
      df_left["Stamina per Distance"] = str(analyzer.used_per_distance_l)

      # print("Right Team :"+analyzer.game.right_team.name + "\n")
      # print("Game result :"+analyzer.status_r)
      # print("Goals :"+str(analyzer.game.right_goal))
      # print("True Pass:"+str(analyzer.pass_r))
      # print("Wrong Pass:"+str(analyzer.intercept_l))
      # print("Pass in Lenght:"+str(analyzer.pass_in_length_r))
      # print("Pass in Width:"+str(analyzer.pass_in_width_r))
      # print("Pass Accuracy:"+str(analyzer.pass_accuracy_r))
      # print("on_target_shoot:"+str(analyzer.on_target_shoot_r))
      # print("off_target_shoot:"+str(analyzer.off_target_shoot_r))
      # print("Shoot in Lenght:"+str(analyzer.shoot_in_length_r))
      # print("Shoot in Width:"+str(analyzer.shoot_in_width_r))
      # print("Shoot Accuracy:"+str(analyzer.shoot_accuracy_r))
      # print("Possession:"+str(analyzer.possession_r))
      # print("Stamina Usage:"+str(analyzer.used_stamina_agents_r))
      # print("moved Distance:"+str(analyzer.team_moved_distance_r))
      # print("Average Distance 10 Player: "+str(analyzer.average_distance_10p_r))
      # print("Average Stamina 10 Player: "+str(analyzer.average_stamina_10p_r))
      # print("Average Stamina Per distance 10 Player: " +str(analyzer.av_st_per_dist_10p_r))
      # print("Stamina per Distance:"+str(analyzer.used_per_distance_r)+"\n"+"\n")
      # print("Left Team :"+analyzer.game.left_team.name+"\n")
      # print("Game result :"+analyzer.status_l)
      # print("Goals :"+str(analyzer.game.left_goal))
      # print("Wrong Pass:"+str(analyzer.intercept_r))
      # print("Pass in Lenght:"+str(analyzer.pass_in_length_l))
      # print("Pass in Width:"+str(analyzer.pass_in_width_l))
      # print("Pass Accuracy:"+str(analyzer.pass_accuracy_l))
      # print("on_target_shoot:"+str(analyzer.on_target_shoot_l))
      # print("off_target_shoot:"+str(analyzer.off_target_shoot_l))
      # print("Shoot in Lenght:"+str(analyzer.shoot_in_length_l))
      # print("Shoot in Width:"+str(analyzer.shoot_in_width_l))
      # print("Shoot Accuracy:"+str(analyzer.shoot_accuracy_l))
      # print("Possession:"+str(analyzer.possession_l))
      # print("Stamina Usage:"+str(analyzer.used_stamina_agents_l))
      # print("moved Distance:"+str(analyzer.team_moved_distance_l))
      # print("Average Distance 10 Player: "+str(analyzer.average_distance_10p_l))
      # print("Average Stamina 10 Player: "+str(analyzer.average_stamina_10p_l))
      # print("Average Stamina Per distance 10 Player: " +
      #       str(analyzer.av_st_per_dist_10p_l))
      # print("Stamina per Distance:"+str(analyzer.used_per_distance_l)+"\n")

      # did not mention these in the csv file!!!!
      for region in analyzer.regions:
          df_right["Ball in Region Percentage "+region.name]=region.ball_in_region_cycles
          df_left["Ball in Region Percentage "+region.name]=region.ball_in_region_cycles
      #     print("Ball in Region Percentage", region.name,
      #           " ", region.ball_in_region_cycles)

      # print("\nRight Team Regions Data")

      # Agent_regions
      # owner_cycles    : cycles player is ball owner in the region
      # position_cycles : cycles player is in the region
      for agent in game.right_team.agents:
          for region in agent.regions:
              df_right[region.name+" "+"Agent number "+str(agent.number)]=" owner_cycles: " +str(region.owner_cycles) + "  " + "position_cycles: "+str(region.position_cycles)
            #   print(region.name+" "+"Agent number "+str(agent.number)+" owner_cycles: " +
            #         str(region.owner_cycles) + "  " + "position_cycles: "+str(region.position_cycles))

      # print("\nLeft Team Regions Data")
      for agent in game.left_team.agents:
          for region in agent.regions:
            df_left[region.name+" "+"Agent number "+str(agent.number)]=" owner_cycles: " +str(region.owner_cycles) + "  " + "position_cycles: "+str(region.position_cycles)

            #   print(region.name+" "+"Agent number "+str(agent.number)+" owner_cycles: " +
                  #   str(region.owner_cycles) + "  " + "position_cycles: "+str(region.position_cycles))
      all_games.append([df_right,df_left])

# # Drawing Heatmap of the game
# heatmap = analyzer.draw_heatmap(right_team=True, left_team=True)

result=pd.DataFrame()
for i,game_res in enumerate(all_games):
     temp_right=pd.DataFrame.from_dict(game_res[0],orient='index',columns=[game_res[0]['Right Team']])
     temp_left=pd.DataFrame.from_dict(game_res[1],orient='index',columns=[game_res[1]['Left Team']])
     temp_right.drop(['Right Team'],inplace=True)
     temp_left.drop(['Left Team'],inplace=True)
     temp_df=pd.concat([temp_left,temp_right],axis=1)
     result = pd.concat([result, temp_df],join='outer',axis=1)
     result.insert(result.shape[1],f"empty{i}",value=[' ']*result.shape[0])

result.to_csv("result.csv")
