# get the files under the 'assets' folder
# and convert them to pngs

# create the 'assets-png' folder if it doesn't exist'
if (!(Test-Path -Path .\assets-png)) {
    md .\assets-png
}

# create the 'info.csv' file if it doesn't exist'
# wipe it if it does exist
if (!(Test-Path -Path .\assets-png\info.csv)) {
    New-Item -Path .\assets-png\info.csv -ItemType File
} else {
    Clear-Content -Path .\assets-png\info.csv
}

# get the files under the 'assets' folder
$files = Get-ChildItem -Path .\assets\*.gif

foreach ($file in $files) {
    # use the magick convert command to convert the gif to multiple pngs
    magick convert $file -coalesce .\assets-png\$($file.BaseName).png
    # count the number of pngs created
    $num_pngs = (Get-ChildItem -Path .\assets-png\$($file.BaseName)*.png).Count
    # write the information to the csv file along with the original gif file name
    Add-Content -Path .\assets-png\info.csv -Value "$($file.BaseName),$num_pngs"
}
