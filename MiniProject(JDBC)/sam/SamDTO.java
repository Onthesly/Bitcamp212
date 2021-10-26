package net.bit.sam;

public class SamDTO {
	private int id;
	private String name;
	private String country;
	private String grade;
	private String speciality;
	private int generalship;
	private int strength;
	private int intellect;
	
	public SamDTO(int id, String name, String country) {
		super();
		this.id = id;
		this.name = name;
		this.country = country;
	}
	
	public SamDTO(int id, String name, String country, String grade, String speciality, int generalship, int strength, int intellect) {
		super();
		this.id = id;
		this.name = name;
		this.country = country;
		this.grade = grade;
		this.speciality = speciality;
		this.generalship = generalship;
		this.strength = strength;
		this.intellect = intellect;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getCountry() {
		return country;
	}
	public void setCountry(String country) {
		this.country = country;
	}
	
	public String getGrade() {
		return grade;
	}

	public void setGrade(String grade) {
		this.grade = grade;
	}

	public String getSpeciality() {
		return speciality;
	}

	public void setSpeciality(String speciality) {
		this.speciality = speciality;
	}

	public int getGeneralship() {
		return generalship;
	}

	public void setGeneralship(int generalship) {
		this.generalship = generalship;
	}

	public int getStrength() {
		return strength;
	}

	public void setStrength(int strength) {
		this.strength = strength;
	}

	public int getIntellect() {
		return intellect;
	}

	public void setIntellect(int intellect) {
		this.intellect = intellect;
	}
	
}
