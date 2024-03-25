from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class City(BaseModel):
    name: str


class WorkExperience(BaseModel):
    name: str


class WorkFormat(BaseModel):
    name: str


class KeySkills(BaseModel):
    name: str


class CompanyName(BaseModel):
    name: str


class Salary(BaseModel):
    minimal: Optional[int] = Field(alias='from')
    maximum: Optional[int] = Field(alias='to')
    currency: Optional[str]


class Vacancy(BaseModel):
    link: str = Field(alias='alternate_url')
    job_title: str = Field(alias='name')
    salary: Optional[Salary]
    company_name: CompanyName = Field(alias='employer')
    city: City = Field(alias='area')
    work_experience: WorkExperience = Field(alias='experience')
    work_format: WorkFormat = Field(alias='employment')
    key_skills: list[KeySkills]
    publication_date: datetime = Field(alias='published_at')

    def get_value(self) -> dict:
        salary = ', '.join(f'{h} {j[1]}' if j[1] else f'{h} Не указано' for h, j in
                           zip(['От', 'До', 'Валюта'], self.salary)) if self.salary else 'Не указано'
        key_skills = ', '.join(skill.name for skill in self.key_skills)
        publication_date = self.publication_date.strftime("%Y-%m-%d %H:%M:%S")
        params = {'link': self.link, 'job_title': self.job_title, 'salary': salary,
                  'company_name': self.company_name.name, 'city': self.city.name,
                  'work_experience': self.work_experience.name, 'work_format': self.work_format.name,
                  'key_skills': key_skills, 'publication_date': publication_date}

        return params



