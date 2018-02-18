xlsxj = require("xlsx-to-json");
  xlsxj({
    input: "SpaceAndScienceReviews.xlsx", 
    output: "SpaceAndScienceReviews.json",

  }, function(err, result) {
    if(err) {
      console.error(err);
    }else {
      console.log(result);
    }
  });
