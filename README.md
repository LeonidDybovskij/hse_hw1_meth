## CpG DNA methylation

[This README in russian](README.ru.md)

The purpose of this work was to study changes in the level of CpG DNA methylation during early embryonic development of the mouse.  
In the early stages, CpG methylation is expected to be minimal (25%), after which it increases to 90% and remains so throughout life.  

This work examines three stages of mouse development during the first week after fertilization:  
8cell - 8-cell embryo (SRR5836473)  
ICM - Inner cell mass (SRR5836475)  
Epiblast - epiblast stage (SRR3824222)

All commands were executed in the Linux terminal.  
Screenshots and text for executing are in the proof folder.

Statistics on the number of reads:
|Number of reads in the area|8 cell|Epiblast|ICM|
|---|---|---|---|
|11347700-11367700|1090|2328|1456|
|40185800-40195800|464|1062|630|

Duplication statistics:
|Duplications|8 cell|Epiblast|ICM|
|---|---|---|---|
|Total|521904|205258|377882|
|Percent|18.31%|2.92%|9.08%|

Bismark reports:

# For stage 8 cell:
![Screenshot from 2022-02-21 23-19-23](https://user-images.githubusercontent.com/60808642/155021722-6951c6c3-5e32-4967-9657-dfedfcc57a30.png)
![Screenshot from 2022-02-21 23-19-35](https://user-images.githubusercontent.com/60808642/155021789-77457d7c-aa6a-4645-8de5-8dee04d1b039.png)
![Screenshot from 2022-02-21 23-19-46](https://user-images.githubusercontent.com/60808642/155022644-3ae240da-5446-48ee-a86e-d1e87ed416e8.png)
![8 cell](https://user-images.githubusercontent.com/60808642/154995957-dc9efa1d-071c-4730-b5c7-944dfc09734d.png)

# For ICM stage:
![Screenshot from 2022-02-21 23-25-40](https://user-images.githubusercontent.com/60808642/155022349-1d4dc970-862b-42d6-ae3d-9bf1ad4eb421.png)
![Screenshot from 2022-02-21 23-25-44](https://user-images.githubusercontent.com/60808642/155022395-92853f91-ae9d-4c02-9215-f27e2c8121a7.png)
![Screenshot from 2022-02-21 23-23-28](https://user-images.githubusercontent.com/60808642/155022558-b09e6244-bddb-41c1-8672-bd488f7f9bf6.png)
![ICM](https://user-images.githubusercontent.com/60808642/154996003-66df01e7-bf5b-44d6-8954-4b69a1369f98.png)

# For Epiblast stage:
![Screenshot from 2022-02-21 23-23-21](https://user-images.githubusercontent.com/60808642/155022052-902b45c4-9fb2-42ac-9e80-533176be13ae.png)
![Screenshot from 2022-02-21 23-23-25](https://user-images.githubusercontent.com/60808642/155022061-513f568a-6754-4123-bacb-6dfa764424ba.png)
![Screenshot from 2022-02-21 23-23-28](https://user-images.githubusercontent.com/60808642/155022071-cc8e424b-6c6d-4bda-997b-7ddbe56238a0.png)
![Epiblast](https://user-images.githubusercontent.com/60808642/154995981-bb2dd211-e909-40a8-a5da-a3fbc257a0e0.png)

As can be seen, the maximum level of CpG methylation is observed at the epiblast stage. Slightly lower at the 8-cell stage and very low at the stage in between, which is generally in line with expectations.

# Histograms of methylated cytosines

These histograms were built using a python script (src folder).  
The X-axis indicates the percentage of methylated cytosines, and the Y-axis indicates the frequency of methylation.

![hw1_eight_cell](https://user-images.githubusercontent.com/60808642/195834753-ddbf1012-3528-40c0-aea5-52bbf1cb9cb8.png)
![hw1_icm](https://user-images.githubusercontent.com/60808642/195834777-7944f5a7-b90c-468f-8c9a-c97b76ef05ae.png)
![hw1_epiblast](https://user-images.githubusercontent.com/60808642/195834791-d17f723d-4748-4ac0-bbaf-9d75b209d301.png)

From these diagrams it can be seen that there are slightly more unmethylated areas than methylated ones at the first stage (8 cell), significantly more at the second stage (icm) and very few at the third stage (epiblast). The percentage of partially methylated regions is not very high for all samples.

Finally, the methylation and coverage levels for each sample (methylation folder) were visualized using pyGenomeTracks.  
Thus, 6 diagrams of the following type were obtained:

![epiblast_11327700-11367700_met](https://user-images.githubusercontent.com/60808642/195835635-53ba3c3b-2ac1-4395-826b-90482be2f3ab.png)
