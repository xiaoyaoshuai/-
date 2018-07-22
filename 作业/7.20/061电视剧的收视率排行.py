a = {'《Give up,hold on to me》收视率:':'1.4%','《The private dishes of the husbands》收视率:':'1.343%','《My father-in-lawwill do martiaiarts》收视率':'0.92%','《North Canton still believe in love》收视率:':'0.553%','《Impossible task》收视率:':'0.553%','《Sparrow》收视率:':'0.411%','《East of dream Avenue》收视率':'0.164%','《The prodigal son of the new frontier town》收视率:':'0.259%','《Distant distance》收视率:':'0.394%','《Music legend》收视率:':'0.562%'}
for i,v in sorted(a.items(),key=lambda item:item[1]):
    print(i,v)
