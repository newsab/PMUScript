import pynmea2
import serial


stream = serial.Serial('/dev/ttyAMA0', 115200)



for sentence in stream:
  try:
    pNMEA = pynmea2.parse(sentence)
    if isinstance(pNMEA, pynmea2.types.talker.GGA):
      print "GGA"
      print '\tTimestamp:', pNMEA.timestamp
      print '\tLatitude:', pNMEA.lat
      print '\tLatitude Direction:', pNMEA.lat_dir
      print '\tLongitude:', pNMEA.lon
      print '\tLongitude Direction:',pNMEA.lon_dir
      print '\tGPS Quality Indicator:', pNMEA.gps_qual
      print '\tNumber of Satellites in use:', pNMEA.num_sats
      print '\tHorizontal Dilution of Precision:', pNMEA.horizontal_dil
      print '\tAntenna Alt above sea level (mean):', pNMEA.altitude
      print '\tUnits of altitude (metres):', pNMEA.altitude_units
      print '\tGeoidal Separation:', pNMEA.geo_sep
      print '\tUnits of Geoidal Separation:', pNMEA.geo_sep_units
      print '\tAge of Differential GPS Data (secs):', pNMEA.age_gps_data
      print '\tDifferential Reference Station ID:', pNMEA.ref_station_id

  except:
    pass

