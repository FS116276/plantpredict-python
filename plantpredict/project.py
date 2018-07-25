import requests
from plantpredict import settings
from plantpredict.plant_predict_entity import PlantPredictEntity
from plantpredict.utilities import decorate_all_methods
from plantpredict.error_handlers import handle_refused_connection, handle_error_response


@decorate_all_methods(handle_refused_connection)
@decorate_all_methods(handle_error_response)
class Project(PlantPredictEntity):

    def create(self, name=None, latitude=None, longitude=None, country=None, country_code=None, elevation=None,
               standard_offset_from_utc=None):
        """
        HTTP Request: POST /Project

        Creates a new Project entity in PlantPredict and assigns the uid of the newly created Project to self.id in the
        local object instance. Any attributes (including but not limited to those also assignable via the inputs to
        this method) assigned prior to calling this method will be recorded in the new Project entity in PlantPredict.

        :return: A dictionary containing the project id.
        :rtype: dict
        """

        self.name = name if name is not None else self.name
        self.latitude = latitude if latitude is not None else self.latitude
        self.longitude = longitude if longitude is not None else self.longitude
        self.country = country if country is not None else self.country
        self.country_code = country_code if country_code is not None else self.country_code
        self.elevation = elevation if elevation is not None else self.elevation
        self.standard_offset_from_utc = standard_offset_from_utc if standard_offset_from_utc is not None \
            else self.standard_offset_from_utc

        self.create_url_suffix = "/Project"

        return super(Project, self).create()

    def delete(self):
        """
        HTTP Request: DELETE /Project/{ProjectId}

        Deletes an existing Project entity in PlantPredict. The local instance of the Project entity must have
        attribute self.id identical to the project id of the Project to be deleted.

        :return: A dictionary {"is_successful": True}.
        :rtype: dict
        """

        self.delete_url_suffix = "/Project/{}".format(self.id)

        return super(Project, self).delete()

    def get(self):
        """
        HTTP Request: GET /Project/{Id}

        Retrieves an existing Project entity in PlantPredict and automatically assigns all of its attributes to the
        local Project object instance. The local instance of the Project entity must have attribute self.id identical
        to the project id of the Project to be retrieved.

        :return: A dictionary containing all of the retrieved Project attributes.
        :rtype: dict
        """

        self.get_url_suffix = "/Project/{}".format(self.id)

        return super(Project, self).get()

    def update(self):
        """
        HTTP Request: PUT /Project

        Updates an existing Project entity in PlantPredict using the full attributes of the local Project instance.
        Calling this method is most commonly preceded by instantiating a local instance of Project with a specified
        project id, calling the Project.get() method, and changing any attributes locally.

        :return: A dictionary {"is_successful": True}.
        :rtype: dict
        """
        self.update_url_suffix = "/Project"

        return super(Project, self).update()

    def get_all_predictions(self):
        """
        HTTP Request: GET /Project/{ProjectId}/Prediction

        Retrieves the full attributes of every Prediction associated with the Project.

        :return: A list of dictionaries, each containing the attributes of a Prediction entity.
        :rtype: list of dict
        """

        return requests.get(
            url=settings.BASE_URL + "/Project/{}/Prediction".format(self.id),
            headers={"Authorization": "Bearer " + settings.TOKEN}
        )

    @staticmethod
    def search(latitude, longitude, search_radius=1.0):
        """
        HTTP Request: GET /Project/Search

        :param latitude: North-South coordinate of the Project location, in decimal degrees.
        :type latitude: float
        :param longitude: East-West coordinate of the Project location, in decimal degrees.
        :type longitude: float
        :param search_radius: search radius in miles
        :type search_radius: float
        :return: int, float
        """

        return requests.get(
            url=settings.BASE_URL + "/Project/Search",
            headers={"Authorization": "Bearer " + settings.TOKEN},
            params={'latitude': latitude, 'longitude': longitude, 'searchRadius': search_radius}
        )

    def __init__(self):
        self.name = None
        self.latitude = None
        self.longitude = None
        self.country = None
        self.country_code = None
        self.elevation = None
        self.standard_offset_from_utc = None

        super(Project, self).__init__()
