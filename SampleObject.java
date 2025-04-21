class SampleObject {
  public string name;
  public integer age;
  public string city;
  public DateTime firstSeen;
  private boolean isSenior;
  public SampleObject() {
    name = "";
    age=0;
    city="Harlem";
    firstSeen = new DateTime(today);

    setSenior();
  }
  public SampleObject(string userName, integer howOld, string userCity) {
    name = userName;
    age = howOld;
    city = userCity;
    firstSeen = new DateTime(today);
    setSenior();
  }
  public boolean userIsSenior() {
    return isSenior;
  }
  private void setSenior() {
    isSenior = (age > 60);
  }
  public void setName(string newName) {
    name=newName;
  }
  public string getName() {
    return name;
  }
  
}

SampleObject newObj = new SampleObj();
newObj.name = 'Randy';
newObj.age=900;
newObj.city='Dearing';
SampleObject newObjv2 = new SampleObj("Randy",900, "Dearing");
