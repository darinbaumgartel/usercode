#!/bin/sh


root -l RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_200 > Log_RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_200.txt
root -l RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_225 > Log_RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_225.txt
root -l RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_250 > Log_RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_250.txt
root -l RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_280 > Log_RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_280.txt
root -l RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_300 > Log_RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_300.txt
root -l RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_320 > Log_RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_320.txt
root -l RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_340 > Log_RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_340.txt
root -l RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_400 > Log_RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_400.txt
root -l RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_450 > Log_RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_450.txt
root -l RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_500 > Log_RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_500.txt
root -l RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_600 > Log_RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_600.txt

cat Log*CLA*txt > Log_Total_CLA.txt



grep ">>" Log_Total_CLA.txt > Log_Summary_CLA.txt


