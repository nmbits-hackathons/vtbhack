import { RouteRecord, RouteRecordName } from "vue-router"

const routeTranslations = {
  Home: "Мероприятия",
  Marketplace: "Маркетплейс",
  Collections: "Коллекции",
  Rating: "Рейтинг"
}

export const useNormalizedRoute = (route: RouteRecordName | null | undefined) => {
  if (route)
    return (routeTranslations as any)[route] || route
  else
    return 'Ошибка'
}